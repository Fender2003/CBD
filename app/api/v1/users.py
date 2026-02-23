# User routes
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import get_db
from app.crud import user as crud_user
from app.core.dependencies import get_current_user
from app.core.hashing import Hasher
from app.core.security import create_access_token
from app.schemas.user import UserLogin, UserMe, UserProfileUpdate, LoginResponse
from app.db.models.user import User



router = APIRouter()

@router.post("/register", response_model=schemas.user.UserOut)
def register(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.user.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    return crud.user.create_user(db, user)


@router.post("/login", response_model=LoginResponse)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = crud.user.get_user_by_email(db, user.email)
    if not db_user or not Hasher.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    
    access_token = create_access_token(
        data={
            "sub": db_user.email,          # backward-compatible for existing frontend token parsing
            "user_id": str(db_user.id),    # stable identifier for newer clients
            "email": db_user.email,
        }
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": db_user.id,
        "email": db_user.email,
    }


@router.get("/me", response_model=UserMe)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/profile", response_model=UserMe)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.patch("/profile", response_model=UserMe)
def update_profile(
    updates: UserProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud_user.update_user_profile(db, current_user, updates)
