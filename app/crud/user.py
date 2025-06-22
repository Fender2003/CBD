# crud/user.py
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate
from app.core.hashing import Hasher

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_user(db: Session, user: UserCreate):
    hashed_pw = Hasher.get_password_hash(user.password)
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_pw,
        full_name = user.full_name,
        phone_number=user.phone_number,
        gender=user.gender,
        age=user.age,
        address=user.address,
        city=user.city,
        state=user.state,
    )
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username or Email already exists")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
