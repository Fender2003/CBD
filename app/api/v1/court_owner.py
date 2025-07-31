from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.court_owner import CourtOwnerCreate, CourtOwnerOut
from app.db.session import get_db
from app.crud import court_owner as crud
from uuid import UUID

router = APIRouter()

@router.post("/court-owner/signup", response_model=CourtOwnerOut)
def signup_court_owner(owner_in: CourtOwnerCreate, db: Session = Depends(get_db)):
    existing = db.query(crud.CourtOwner).filter_by(email=owner_in.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_court_owner(db, owner_in)


@router.delete("/court-owner/delete/{owner_id}", response_model=dict)
def delete_court_owner(owner_id: UUID, db: Session = Depends(get_db)):
    owner = db.query(crud.CourtOwner).filter_by(id=owner_id).first()
    if not owner:
        raise HTTPException(status_code=404, detail="Court owner not found")

    db.delete(owner)
    db.commit()
    return {"detail": "Court owner account deleted successfully"}
