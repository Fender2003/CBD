# crud/user.py
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate, UserProfileUpdate
from app.core.hashing import Hasher
from uuid import UUID

from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_user(db: Session, user: UserCreate):
    hashed_pw = Hasher.get_password_hash(user.password)
    db_user = User(
        email=user.email,
        hashed_password=hashed_pw,
        full_name = user.full_name,
        phone_number=user.phone_number,
        gender=user.gender,
        age=user.age,
        address=user.address,
        city=user.city,
        state=user.state
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


def get_user_by_id(db: Session, user_id: UUID):
    return db.query(User).filter(User.id == user_id).first()


def update_user_profile(db: Session, db_user: User, updates: UserProfileUpdate):
    update_data = updates.model_dump(exclude_unset=True)
    if not update_data:
        return db_user

    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user



# def get_user_by_id(db: Session, user_id: int):
#    return db.query(User).filter(User.id == user_id).first()

# def get_all_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(User).offset(skip).limit(limit).all()

# from app.schemas.user import UserUpdate

# def update_user(db: Session, user_id: int, updates: UserUpdate):
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")

#     for key, value in updates.dict(exclude_unset=True).items():
#         setattr(db_user, key, value)

#     db.commit()
#     db.refresh(db_user)
#     return db_user



# def delete_user(db: Session, user_id: int):
#     db_user = db.query(User).filter(User.id == user_id).first()
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")

#     db.delete(db_user)
#     db.commit()
#     return {"message": "User deleted successfully"}



# def verify_user(db: Session, email: str, password: str):
#     user = get_user_by_email(db, email)
#     if not user or not Hasher.verify_password(password, user.hashed_password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     return user
