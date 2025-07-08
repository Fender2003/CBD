from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.group_card import GroupCard
from app.api.v1.match import groupcard_to_dict

router = APIRouter()


@router.post("/group-card/{group_id}/lobby")
def add_to_lobby(group_id: int, db: Session = Depends(get_db)):
    card = db.query(GroupCard).filter_by(group_id=group_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Group card not found")
    
    card.is_in_lobby = True
    db.commit()
    return {"message": "Group added to lobby"}

@router.get("/lobby")
def get_lobby(db: Session = Depends(get_db)):
    groups = db.query(GroupCard).filter_by(is_in_lobby=True).all()
    return {"lobby": [groupcard_to_dict(g) for g in groups]}
