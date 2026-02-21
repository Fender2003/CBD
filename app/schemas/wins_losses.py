from pydantic import BaseModel
from uuid import UUID
from typing import List

class PlayerStats(BaseModel):
    user_id: UUID
    game_wins: int
    game_losses: int
    number_of_games: int
    rating_change: float

class StatsSubmission(BaseModel):
    game_id: UUID
    results: List[PlayerStats]

class PlayerResultOut(BaseModel):
    user_id: UUID
    game_wins: int
    game_losses: int
    number_of_games: int

    class Config:
        from_attributes = True


