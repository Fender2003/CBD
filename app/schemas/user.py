# schemas/user.py

from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str
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
    username: str
    is_verified: bool
    full_name: str
    phone_number: str
    gender: str
    age: int
    address: str
    city: str
    state: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
