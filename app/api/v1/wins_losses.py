from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.db.session import get_db
from app.db.models.completed_game import CompletedGame
from app.db.models.group_card import GroupCard
from app.db.models.group_player import GroupPlayer 
from app.db.models.wins_losses import Wins_losses

import uuid
from app.schemas.wins_losses import StatsSubmission

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
    if game_id != stats.game_id:
        raise HTTPException(status_code=400, detail="Mismatched game ID in path and body.")

    for player in stats.results:
        entry = db.query(Wins_losses).filter_by(game_id=game_id, user_id=player.user_id).first()
        if not entry:
            raise HTTPException(status_code=404, detail=f"No entry found for user {player.user_id} in game {game_id}")

        entry.game_wins = player.game_wins
        entry.game_losses = player.game_losses
        entry.number_of_games = player.number_of_games
        entry.rating_change = player.rating_change

    db.commit()
    return {"detail": "Player stats updated successfully"}
