from sqlalchemy.orm import Session
from app.db.models.sport import Sport
from app.schemas.sport import SportCreate

def create_sport(db: Session, sport: SportCreate):
    db_sport = Sport(sport_name=sport.sport_name)
    db.add(db_sport)
    db.commit()
    db.refresh(db_sport)
    return db_sport

def get_all_sports(db: Session):
    return db.query(Sport).all()
