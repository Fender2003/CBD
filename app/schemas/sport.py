from pydantic import BaseModel
import uuid
class SportBase(BaseModel):
    sport_name: str

class SportCreate(SportBase):
    pass

class SportOut(SportBase):
    sport_id: uuid.UUID
    sport_name: str

    class Config:
        orm_mode = True 
