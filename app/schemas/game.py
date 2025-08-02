from datetime import datetime
from typing import Optional, Dict
from uuid import UUID
from pydantic import BaseModel
from sqlalchemy.orm import relationship


class CompletedGameBase(BaseModel):
    court_id: UUID
    sport_id: UUID
    groupcard1_id: UUID
    groupcard2_id: Optional[UUID]
    winner_group_id: Optional[UUID]

    start_time: datetime
    end_time: datetime
    price: float

    match_type: Optional[str]
    is_rated: Optional[bool] = True

    notes: Optional[str] = None


class CompletedGameCreate(CompletedGameBase):
    pass

class CompletedGameOut(CompletedGameBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
