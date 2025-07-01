from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.court import CourtCreate, CourtOut
from app.crud import court as crud
from app.db.session import get_db

router = APIRouter()

@router.post("/courts/", response_model=CourtOut)
def create_court(court: CourtCreate, db: Session = Depends(get_db)):
    return crud.create_court(db, court)

@router.get("/courts/", response_model=list[CourtOut])
def list_courts(db: Session = Depends(get_db)):
    return crud.get_all_courts(db)
