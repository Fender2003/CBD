from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date, time
from uuid import UUID

class GroupCreate(BaseModel):
    name: str
    leader_id: UUID
    friend_phone_numbers: List[str]


class GroupCardCreate(BaseModel):
    group_id: int
    
    start_time: time
    end_time: time
    booking_date: date