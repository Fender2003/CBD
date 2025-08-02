from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
import uuid
from sqlalchemy.orm import relationship

class Sport(Base):
    __tablename__ = "sport"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    sport_name = Column(String, unique=True, nullable=False)


    completed_games = relationship("CompletedGame", back_populates="sport")
