from sqlalchemy.orm import Session
from app.db.models.court_owner import CourtOwner
from app.schemas.court_owner import CourtOwnerCreate
from app.core.hashing import Hasher

def create_court_owner(db: Session, owner_in: CourtOwnerCreate) -> CourtOwner:
    hashed_pw = Hasher.get_password_hash(owner_in.password)
    db_owner = CourtOwner(
        email=owner_in.email,
        hashed_password=hashed_pw,
        first_name=owner_in.first_name,
        last_name=owner_in.last_name,
        phone_number=owner_in.phone_number,
        age=owner_in.age,
    )
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner
