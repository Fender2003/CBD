# schemas/user.py
from pydantic import BaseModel, EmailStr
import uuid
from datetime import datetime
from typing import Optional

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


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: uuid.UUID
    email: EmailStr


class UserMe(BaseModel):
    id: uuid.UUID
    email: EmailStr
    full_name: str
    phone_number: str
    gender: str
    age: int
    address: str
    city: str
    state: str
    rating: int
    created_at: datetime

    class Config:
        from_attributes = True


class UserProfileUpdate(BaseModel):
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str
