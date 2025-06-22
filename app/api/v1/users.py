# User routes
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app import crud, schemas
from app.db.session import get_db
from app.crud import user as crud_user
from app.core.hashing import Hasher
from app.core import security
from app.core.security import create_access_token
from app.schemas.user import UserLogin



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

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = crud.user.get_user_by_email(db, user.email)
    if not db_user or not Hasher.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
