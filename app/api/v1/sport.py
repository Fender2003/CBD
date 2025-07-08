from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.sport import SportCreate, SportOut
from app.crud.sport import create_sport, get_all_sports
from typing import List

router = APIRouter()

@router.post("/sports/", response_model=SportOut)
def create_new_sport(sport: SportCreate, db: Session = Depends(get_db)):
    return create_sport(db, sport)

@router.get("/sports/", response_model=List[SportOut])
def list_all_sports(db: Session = Depends(get_db)):
    return get_all_sports(db)
