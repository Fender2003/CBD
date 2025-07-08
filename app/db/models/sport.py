from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class Sport(Base):
    __tablename__ = "sport"

    sport_id = Column(Integer, primary_key=True, index=True)
    sport_name = Column(String, unique=True, nullable=False)
