from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
import uuid

class Sport(Base):
    __tablename__ = "sport"

    sport_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    sport_name = Column(String, unique=True, nullable=False)
