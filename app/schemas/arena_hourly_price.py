from pydantic import BaseModel
from uuid import UUID
from datetime import time

class ArenaHourlyPriceBase(BaseModel):
    start_hour: time
    end_hour: time
    price: float

class ArenaHourlyPriceCreate(ArenaHourlyPriceBase):
    arena_id: UUID

class ArenaHourlyPriceResponse(ArenaHourlyPriceBase):
    id: UUID
    arena_id: UUID

    class Config:
        orm_mode = True

