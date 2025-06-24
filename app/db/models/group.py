from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base
from sqlalchemy.dialects.postgresql import UUID

class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    leader_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    date_created = Column(DateTime, default=datetime.utcnow)
    members = relationship("GroupPlayer", back_populates="group")
    