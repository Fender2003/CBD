from pydantic import BaseModel
from typing import Optional
from datetime import date, time
from uuid import UUID


class GroupOut(BaseModel):
    id: UUID
    name: str
    leader_id: UUID

    class Config:
        from_attributes = True

class GroupCardOut(BaseModel):
    id: UUID
    group_id: UUID
    average_age: int
    gender_combo: str
    centroid: Optional[str] = None
    start_time: time
    end_time: time
    booking_date: date
    player_count: int
    arena_id: UUID
    is_in_lobby: bool
    rated: bool
    
    class Config:
        from_attributes = True