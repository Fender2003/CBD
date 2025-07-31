from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class GroupMatchRequest(Base):
    __tablename__ = "group_match_requests"

    id = Column(UUID(as_uuid=True), primary_key=True,  default=uuid.uuid4, nullable=False)
    from_group_id = Column(UUID(as_uuid=True), ForeignKey("group_cards.id"), nullable=False)
    to_group_id = Column(UUID(as_uuid=True), ForeignKey("group_cards.id"), nullable=False)
    status = Column(String, default="pending")  # pending, accepted, rejected
    timestamp = Column(DateTime, default=datetime.utcnow)

    from_group = relationship("GroupCard", foreign_keys=[from_group_id])
    to_group = relationship("GroupCard", foreign_keys=[to_group_id])
