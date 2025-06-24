from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class GroupOut(BaseModel):
    id: int
    name: str
    leader_id: int

    class Config:
        orm_mode = True

class GroupCardOut(BaseModel):
    id: int
    group_id: int
    gender_age: int
    gender_combo: str
    centroid: Optional[str] = None

    class Config:
        orm_mode = True
