from sqlalchemy import Column, Integer, String, Time, Float
from app.db.base_class import Base

class Court(Base):
    __tablename__ = "court"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)
    
    number_of_courts = Column(Integer, nullable=False)
    opening_time = Column(Time, nullable=False)
    closing_time = Column(Time, nullable=False)

    latitude = Column(Float, nullable = False)
    longitude = Column(Float, nullable = False)
