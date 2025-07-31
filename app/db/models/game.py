from sqlalchemy import Column, DateTime, Float, ForeignKey, String, Text, Boolean
from sqlalchemy.dialects.postgresql import UUID, JSONB
from datetime import datetime
import uuid

from app.db.base_class import Base

class CompletedGame(Base):
    __tablename__ = "completed_games"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    court_id = Column(UUID(as_uuid=True), ForeignKey("courts.id"), nullable=False)
    groupcard1_id = Column(UUID(as_uuid=True), ForeignKey("group_card.id"), nullable=False)
    groupcard2_id = Column(UUID(as_uuid=True), ForeignKey("group_card.id"), nullable=True)
    winner_group_id = Column(UUID(as_uuid=True), ForeignKey("group_card.id"), nullable=True)

    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    price = Column(Float, nullable=False)

    match_type = Column(String, nullable=True)
    is_rated = Column(Boolean, default=True)
    rating_change = Column(JSONB, nullable=True)

    notes = Column(Text, nullable=True)
    match_completed = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)

