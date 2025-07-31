from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from sqlalchemy import Time

class ArenaHourlyPrice(Base):
    __tablename__ = "arena_hourly_prices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    arena_id = Column(UUID(as_uuid=True), ForeignKey("arenas.id"), nullable=False)

    start_hour = Column(Time, nullable=False)
    end_hour = Column(Time, nullable=False)
    price = Column(Float, nullable=False)

    arena = relationship("Arena", back_populates="hourly_prices")
