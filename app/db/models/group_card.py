from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.db.base_class import Base
from sqlalchemy import Time, Date
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID


class GroupCard(Base):
    __tablename__ = "group_cards"

    id = Column(UUID(as_uuid=True), primary_key=True,  default=uuid.uuid4, nullable=False)
    group_id = Column(UUID(as_uuid=True), ForeignKey("groups.id"))
    group = relationship("Group", back_populates="group_card")

    average_age = Column(Integer)
    gender_combo = Column(String)
    centroid = Column(String)

    start_time = Column(Time)
    end_time = Column(Time)
    booking_date = Column(Date)

    player_count = Column(Integer)

    # court_id = Column(UUID(as_uuid=True))
    arena_id = Column(UUID(as_uuid=True), ForeignKey("arenas.id"))
    is_in_lobby = Column(Boolean, default=False)
    rated = Column(Boolean, default=False)
    
    group = relationship("Group", back_populates="group_card")
