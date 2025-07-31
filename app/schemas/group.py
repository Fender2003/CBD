from pydantic import BaseModel
from typing import List
from datetime import date, time
from uuid import UUID
from enum import Enum 

class MatchTypeEnum(str, Enum): 
    singles = "singles"
    doubles = "doubles"

class GroupCreate(BaseModel):

    match_type: MatchTypeEnum
    name: str
    leader_id: UUID
    friend_phone_numbers: List[str]

class GroupCardCreate(BaseModel):
    group_id: UUID

    start_time: time
    end_time: time
    booking_date: date
    arena_id: UUID
    rated: bool

