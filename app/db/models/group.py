from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import date, time, datetime
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    match_type = Column(String, nullable=False, default='doubles')
    name = Column(String)
    leader_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    # start_time = time
    # end_time = time
    # booking_date = date
    
    date_created = Column(DateTime, default=datetime.utcnow)
    members = relationship("GroupPlayer", back_populates="group")

    group_card = relationship("GroupCard", back_populates="group", uselist=False)


