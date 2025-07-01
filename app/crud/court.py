from sqlalchemy.orm import Session
from app.db.models.court import Court
from app.schemas.court import CourtCreate

def create_court(db: Session, court: CourtCreate):
    db_court = Court(**court.dict())
    db.add(db_court)
    db.commit()
    db.refresh(db_court)
    return db_court

def get_all_courts(db: Session):
    return db.query(Court).all()
