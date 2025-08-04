# app/schemas/completed_game.py

from pydantic import BaseModel
from uuid import UUID

class CompleteGameRequest(BaseModel):
    match_req_id: UUID
