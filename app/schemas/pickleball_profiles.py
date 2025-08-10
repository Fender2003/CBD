from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class PickleballProfileBase(BaseModel):
    user_id: UUID
    total_wins: int
    total_losses: int
    rated_games: int
    unrated_games: int
    rating_sequence: str
    rating: float


class PickleballProfileCreate(BaseModel):
    user_id: UUID


class PickleballProfileUpdate(BaseModel):
    total_wins: Optional[int] = None
    total_losses: Optional[int] = None
    rated_games: Optional[int] = None
    unrated_games: Optional[int] = None
    rating_sequence: Optional[str] = None
    rating: Optional[float] = None


class PickleballProfileOut(PickleballProfileBase):
    id: UUID

    class Config:
        orm_mode = True
