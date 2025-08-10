from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.db.base_class import Base  # assuming you have a base class

class PickleballProfile(Base):
    __tablename__ = "pickleball_profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)

    total_wins = Column(Integer, default=0)
    total_losses = Column(Integer, default=0)
    rated_games = Column(Integer, default=0)
    unrated_games = Column(Integer, default=0)
    rating_sequence = Column(String, default="")  # e.g., "+5,-2,+7,-1"
    rating = Column(Float, default=1000.0)
    
    user = relationship("User", back_populates="pickleball_profile")  # Optional, if bidirectional


