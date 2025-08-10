from sqlalchemy import Column, DateTime, Float, ForeignKey, String, Text, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid

from app.db.base_class import Base

class Wins_losses(Base):
    __tablename__ = "wins_losses"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    game_id = Column(UUID(as_uuid=True), ForeignKey("completed_game.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    game_wins = Column(Integer)
    game_losses = Column(Integer)
    number_of_games = Column(Integer)
    rating_change = Column(Float)

    # game = relationship("CompletedGame", back_populates="wins_losses")
    user = relationship("User", back_populates="wins_losses")

    completed_game = relationship("CompletedGame", back_populates="wins_losses")
