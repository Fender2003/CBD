from pydantic import BaseModel
from datetime import time

class CourtCreate(BaseModel):
    name: str
    address: str
    city: str
    state: str
    contact_number: str
    number_of_courts: int
    opening_time: time
    closing_time: time
    latitude: float
    longitude: float

class CourtOut(CourtCreate):
    id: int

    class Config:
        from_attributes = True
