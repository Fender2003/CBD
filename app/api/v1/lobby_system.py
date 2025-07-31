from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.group_card import GroupCard
from app.api.v1.match import groupcard_to_dict
from uuid import UUID
router = APIRouter()


@router.post("/group-card/{group_card_id}/lobby")
def add_to_lobby(group_card_id: UUID, db: Session = Depends(get_db)):
    card = db.query(GroupCard).filter(GroupCard.id == group_card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Group card not found")

    card.is_in_lobby = True
    db.commit()
    return {"message": "Group added to lobby"}



@router.post("/group-card/{group_card_id}/leave-lobby")
def leave_lobby(group_card_id: UUID, db: Session = Depends(get_db)):
    group_card = db.query(GroupCard).filter(GroupCard.id == group_card_id).first()
    if not group_card:
        raise HTTPException(status_code=404, detail="Group card not found")

    if not group_card.is_in_lobby:
        return {"message": "Group is already not in the lobby"}

    group_card.is_in_lobby = False
    db.commit()
    return {"message": "Group removed from the lobby"}



@router.get("/lobby")
def get_lobby(db: Session = Depends(get_db)):
    groups = db.query(GroupCard).filter_by(is_in_lobby=True).all()
    return {"lobby": [groupcard_to_dict(g) for g in groups]}

