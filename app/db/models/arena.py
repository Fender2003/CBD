from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import uuid

class Arena(Base):
    __tablename__ = "arenas"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    num_courts = Column(Integer, nullable=False)
    court_type = Column(String, nullable=False)
    
    arena_handler_name = Column(String, nullable=False)
    arena_handler_contact = Column(String, nullable=False)

    owner_id = Column(UUID(as_uuid=True), ForeignKey("court_owners.id"), nullable=False)
    owner = relationship("CourtOwner", back_populates="arenas")
    
    hourly_prices = relationship("ArenaHourlyPrice", back_populates="arena", cascade="all, delete-orphan")

    location_coordinates = Column(JSONB, nullable=True)
