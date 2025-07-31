from pydantic import BaseModel
from uuid import UUID
from typing import Optional, Dict

class ArenaBase(BaseModel):
    name: str
    location: str
    num_courts: int
    court_type: str
    arena_handler_name: str
    arena_handler_contact: str

    location_coordinates: Optional[Dict[str, float]] = None

class ArenaCreate(ArenaBase):
    owner_id: UUID

class ArenaOut(ArenaBase):
    id: UUID

    class Config:
        orm_mode = True
