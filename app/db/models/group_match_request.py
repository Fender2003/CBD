from sqlalchemy import Column, ForeignKey, String, DateTime, Index
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base_class import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class GroupMatchRequest(Base):
    __tablename__ = "group_match_requests"
    __table_args__ = (
        Index("ix_group_match_requests_from_group_id", "from_group_id"),
        Index("ix_group_match_requests_to_group_id", "to_group_id"),
        Index("ix_group_match_requests_status", "status"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    from_group_id = Column(UUID(as_uuid=True), ForeignKey("group_cards.id"), nullable=False)
    to_group_id = Column(UUID(as_uuid=True), ForeignKey("group_cards.id"), nullable=False)
    status = Column(String, default="pending")  # pending, accepted, rejected
    timestamp = Column(DateTime, default=datetime.utcnow)

    from_group = relationship("GroupCard", foreign_keys=[from_group_id])
    to_group = relationship("GroupCard", foreign_keys=[to_group_id])
