from sqlalchemy import Column, Float, ForeignKey,DateTime, String, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from sqlalchemy import Time, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class CompletedGame(Base):
    __tablename__ = "completed_game"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    match_req_id = Column(UUID(as_uuid=True), ForeignKey("group_match_requests.id"), nullable=False)
    court_id = Column(UUID(as_uuid=True), ForeignKey("arenas.id"), nullable=False)
    sport_id = Column(UUID(as_uuid=True), ForeignKey("sport.id"), nullable=False)
    groupcard1_id = Column(UUID(as_uuid=True), ForeignKey("group_cards.id"), nullable=False)
    groupcard2_id = Column(UUID(as_uuid=True), ForeignKey("group_cards.id"), nullable=True)
    # winner_group_id = Column(UUID(as_uuid=True), ForeignKey("group_card.id"), nullable=True)

    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    bookibg_date = Column(Date, nullable=False)
    price = Column(Float, nullable=False)

    match_type = Column(String, nullable=True)
    is_rated = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.utcnow)



    sport = relationship("Sport", back_populates="completed_games")
    arena = relationship("Arena", back_populates="completed_games")

    groupcard1 = relationship("GroupCard", foreign_keys=[groupcard1_id])
    groupcard2 = relationship("GroupCard", foreign_keys=[groupcard2_id])

    wins_losses = relationship("Wins_losses", back_populates="completed_game")
