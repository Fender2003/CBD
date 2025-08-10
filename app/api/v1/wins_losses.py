from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.session import get_db
from app.db.models.completed_game import CompletedGame
from app.db.models.group_card import GroupCard
from app.db.models.group_player import GroupPlayer 
from app.db.models.wins_losses import Wins_losses
from app.db.models.pickleball_profiles import PickleballProfile
from app.ds.rating_change import calculate_rating_change
import uuid
from app.schemas.wins_losses import StatsSubmission
import traceback


router = APIRouter()

@router.post("/games/{game_id}/prepare-wins-losses")
def prepare_wins_losses_entries(game_id: UUID, db: Session = Depends(get_db)):
    game = db.query(CompletedGame).filter(CompletedGame.id == game_id).first()
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")

    groupcard_ids = [game.groupcard1_id]
    if game.groupcard2_id:
        groupcard_ids.append(game.groupcard2_id)

    player_ids = set()

    for groupcard_id in groupcard_ids:
        group_card = db.query(GroupCard).filter(GroupCard.id == groupcard_id).first()
        if not group_card:
            raise HTTPException(status_code=404, detail=f"GroupCard {groupcard_id} not found")

        group_players = db.query(GroupPlayer).filter(GroupPlayer.group_id == group_card.group_id).all()
        for gp in group_players:
            player_ids.add(gp.user_id)

    created_entries = []
    for user_id in player_ids:
        # Check if already exists
        existing = db.query(Wins_losses).filter_by(game_id=game_id, user_id=user_id).first()
        if existing:
            continue

        entry = Wins_losses(
            id=uuid.uuid4(),
            game_id=game_id,
            user_id=user_id,
            game_wins=0,
            game_losses=0,
            number_of_games=0,
            rating_change=0
        )
        db.add(entry)
        created_entries.append(str(user_id))

    db.commit()
    return {
        "detail": f"Created wins_losses entries for {len(created_entries)} players",
        "user_ids": created_entries
    }



@router.post("/games/{game_id}/submit-results")
def submit_match_results(game_id: UUID, stats: StatsSubmission, db: Session = Depends(get_db)):


    try:
        if game_id != stats.game_id:
            raise HTTPException(status_code=400, detail="Mismatched game ID in path and body.")

        total_wins = 0
        total_losses = 0

        game_counts = []
        wins_list = []
        losses_list = []

        for player in stats.results:
            # Rule 1: Player's wins + losses == number_of_games
            if player.game_wins + player.game_losses != player.number_of_games:
                raise HTTPException(
                    status_code=400,
                    detail=f"Inconsistent stats for user {player.user_id}: wins + losses != total games played"
                )

            total_wins += player.game_wins
            total_losses += player.game_losses

            game_counts.append(player.number_of_games)
            wins_list.append(player.game_wins)
            losses_list.append(player.game_losses)

        # Rule 2: Total wins == total losses
        if total_wins != total_losses:
            raise HTTPException(
                status_code=400,
                detail=f"Total wins ({total_wins}) do not match total losses ({total_losses})"
            )

        player_count = len(stats.results)

        # Rule 3: Extra check for 2 players
        if player_count == 2:
            p1, p2 = stats.results

            if p1.number_of_games != p2.number_of_games:
                raise HTTPException(status_code=400, detail="In 1v1 matches, both players must have played the same number of games.")

            if p1.game_wins != p2.game_losses or p2.game_wins != p1.game_losses:
                raise HTTPException(status_code=400, detail="In 1v1 matches, one player's wins must equal the other's losses.")

        # Fetch rating flag from the completed_game table
        completed_game = db.query(CompletedGame).filter_by(id=game_id).first()
        if not completed_game:
            raise HTTPException(status_code=404, detail=f"Game {game_id} not found in CompletedGame table.")

        is_rated = completed_game.is_rated

        try:
            player_ratings = {}
            past_game_count = {}
            for player in stats.results:
                profile = db.query(PickleballProfile).filter_by(user_id=player.user_id).first()
                if profile is None:
                    player_ratings[player.user_id] = 1000.0
                    past_game_count[player.user_id] = 0
                else:
                    print("profile found")
                    player_ratings[player.user_id] = profile.rating if profile.rating is not None else 1000.0
                    past_game_count[player.user_id] = profile.rated_games if profile.rated_games is not None else 0
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail=str(e))

        print(past_game_count)
        # Loop through players to update profiles
        for player in stats.results:
            win_loss_entry = db.query(Wins_losses).filter_by(game_id=game_id, user_id=player.user_id).first()
            if not win_loss_entry:
                raise HTTPException(status_code=404, detail=f"Wins_losses entry not found for user {player.user_id}")

            # Calculate opponent average rating
            opponents = [uid for uid in player_ratings.keys() if uid != player.user_id]
            opponent_avg_rating = sum(player_ratings[uid] for uid in opponents) / len(opponents)
            player_game_count = past_game_count[player.user_id]

            rating_change = 0.0
            if is_rated:
                rating_change = calculate_rating_change(
                    current_rating=player_ratings[player.user_id],
                    opponent_avg_rating=opponent_avg_rating,
                    game_wins=player.game_wins,
                    game_losses=player.game_losses,
                    past_game_count=player_game_count
                )

            # Update Wins_losses
            win_loss_entry.game_wins = player.game_wins
            win_loss_entry.game_losses = player.game_losses
            win_loss_entry.number_of_games = player.number_of_games
            win_loss_entry.rating_change = rating_change

            # Update profile
            profile = db.query(PickleballProfile).filter_by(user_id=player.user_id).first()
            if not profile:
                profile = PickleballProfile(
                    user_id=player.user_id,
                    total_wins=0,
                    total_losses=0,
                    rated_games=0,
                    unrated_games=0,
                    rating_sequence="",
                    rating=1000.0
                )
                db.add(profile)

            profile.total_wins += player.game_wins
            profile.total_losses += player.game_losses

            if is_rated:
                profile.rated_games += player.number_of_games
                profile.rating += rating_change
                if profile.rating_sequence:
                    profile.rating_sequence += f",{rating_change:+.2f}"
                else:
                    profile.rating_sequence = f"{rating_change:+.2f}"
            else:
                profile.unrated_games += player.number_of_games

        db.commit()

        return {"detail": "Player stats updated successfully"}

    except Exception as e:

        print("b")
        print(e)
        print("a")
        traceback.print_exc()

        raise HTTPException(status_code=500, detail=str(e))