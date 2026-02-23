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


class GroupCardUpdate(BaseModel):
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    booking_date: Optional[date] = None
    rated: Optional[bool] = None
    arena_id: Optional[UUID] = None


class MyLobbyGroupCardOut(BaseModel):
    group_card_id: UUID
    group_id: UUID
    match_type: str
    booking_date: date
    start_time: time
    end_time: time
    arena_id: UUID
    rated: bool
    player_count: int
    is_in_lobby: bool
