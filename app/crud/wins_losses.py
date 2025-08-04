# crud/wins_losses.py

from sqlalchemy.orm import Session
from app.db.models.wins_losses import Wins_losses
from app.schemas.wins_losses import WinsLossesCreate
from uuid import UUID

def create_wins_losses_entry(db: Session, game_id: UUID, entry: WinsLossesCreate):
    db_entry = Wins_losses(
        game_id=game_id,
        user_id=entry.user_id,
        game_wins=entry.game_wins,
        game_losses=entry.game_losses,
        number_of_games=entry.number_of_games,
        rating_change=entry.rating_change
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
