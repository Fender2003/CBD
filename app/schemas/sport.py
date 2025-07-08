from pydantic import BaseModel

class SportBase(BaseModel):
    sport_name: str

class SportCreate(SportBase):
    pass

class SportOut(SportBase):
    sport_id: int

    class Config:
        orm_mode = True 
