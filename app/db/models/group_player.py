from sqlalchemy import Column, Integer, ForeignKey
from app.db.base_class import Base
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID


class GroupPlayer(Base):
    __tablename__ = "group_players"

    id = Column(UUID(as_uuid=True), primary_key=True,  default=uuid.uuid4, nullable=False)
    group_id = Column(UUID(as_uuid=True), ForeignKey("groups.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    group = relationship("Group", back_populates="members")
