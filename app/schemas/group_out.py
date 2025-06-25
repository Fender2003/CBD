from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date, time
from uuid import UUID


class GroupOut(BaseModel):
    id: int
    name: str
    leader_id: UUID

    class Config:
        orm_mode = True

class GroupCardOut(BaseModel):
    id: int
    group_id: int
    average_age: int
    gender_combo: str
    centroid: Optional[str] = None
    start_time: time
    end_time: time
    booking_date: date
    player_count: int
    
    class Config:
        orm_mode = True
