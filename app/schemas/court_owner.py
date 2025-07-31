from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class CourtOwnerCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone_number: str
    age: int | None = None

class CourtOwnerOut(BaseModel):
    id: UUID
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: str
    age: int | None = None
    created_at: datetime

    class Config:
        orm_mode = True
