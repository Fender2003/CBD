from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base

class GroupMatchRequest(Base):
    __tablename__ = "group_match_requests"

    id = Column(Integer, primary_key=True, index=True)
    from_group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    to_group_id = Column(Integer, ForeignKey("groups.id"), nullable=False)
    status = Column(String, default="pending")  # pending, accepted, rejected
    timestamp = Column(DateTime, default=datetime.utcnow)

    from_group = relationship("Group", foreign_keys=[from_group_id])
    to_group = relationship("Group", foreign_keys=[to_group_id])
