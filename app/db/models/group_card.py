from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Index
from app.db.base_class import Base
from sqlalchemy import Time, Date
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID


class GroupCard(Base):
    __tablename__ = "group_cards"
    __table_args__ = (
        Index("ix_group_cards_group_id", "group_id"),
        Index("ix_group_cards_is_in_lobby", "is_in_lobby"),
        Index("ix_group_cards_rated", "rated"),
        Index("ix_group_cards_player_count", "player_count"),
        Index("ix_group_cards_booking_date", "booking_date"),
        Index("ix_group_cards_start_time", "start_time"),
        Index("ix_group_cards_end_time", "end_time"),
        Index(
            "ix_group_cards_challenge_lobby",
            "is_in_lobby",
            "rated",
            "player_count",
            "booking_date",
            "start_time",
            "end_time",
        ),
    )

    id = Column(UUID(as_uuid=True), primary_key=True,  default=uuid.uuid4, nullable=False)
    group_id = Column(UUID(as_uuid=True), ForeignKey("groups.id"))
    

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
