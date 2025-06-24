from sqlalchemy import Column, Integer, ForeignKey
from app.db.base_class import Base
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy.dialects.postgresql import UUID

class GroupPlayer(Base):
    __tablename__ = "group_players"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey("group.id"))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

    group = relationship("Group", back_populates="members")
