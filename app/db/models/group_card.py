from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db.base_class import Base
from datetime import datetime, date, time
from sqlalchemy import Time, Date

class GroupCard(Base):
    __tablename__ = "group_cards"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey("group.id"))
    average_age = Column(Integer)
    gender_combo = Column(String)
    centroid = Column(String)

    start_time = Column(Time)
    end_time = Column(Time)
    booking_date = Column(Date)

    player_count = Column(Integer)
