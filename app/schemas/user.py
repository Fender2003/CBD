# schemas/user.py

from pydantic import BaseModel, EmailStr
import uuid

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    phone_number: str
    gender: str
    age: int
    address: str
    city: str
    state: str

class UserOut(BaseModel):
    id: uuid.UUID
    email: EmailStr
    is_verified: bool
    full_name: str
    phone_number: str
    gender: str
    age: int
    address: str
    city: str
    state: str
    rating: int

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
