from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import ValidationError
from app.schemas.group import GroupCreate, GroupCardCreate
from app.schemas.group_card import GroupOut, GroupCardOut, GroupCardUpdate, MyLobbyGroupCardOut
from app.db.session import get_db
from app.crud import group as crud_group
from app.core.dependencies import get_current_user
from app.db.models.user import User
from app.db.models.group_card import GroupCard
from uuid import UUID

router = APIRouter()

@router.post("/create", response_model=GroupOut)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    return crud_group.create_group(db, group.match_type, group.name, group.leader_id, group.friend_phone_numbers)

@router.post("/card", response_model=GroupCardOut)
def create_group_card(data: GroupCardCreate, db: Session = Depends(get_db)):
    return crud_group.create_group_card(db, data.group_id, data.start_time, data.end_time, data.booking_date, data.arena_id, data.rated)


@router.get("/my-lobby", response_model=list[MyLobbyGroupCardOut])
def get_my_lobby_groups(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud_group.get_my_lobby_group_cards(db, current_user.id)


@router.patch("/card/{group_card_id}", response_model=GroupCardOut)
def update_group_card(
    group_card_id: UUID,
    updates_payload: dict = Body(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        updates = GroupCardUpdate.model_validate(updates_payload)
    except ValidationError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.errors()) from exc

    group_card = crud_group.get_group_card_owned_by_leader(db, group_card_id, current_user.id)
    if not group_card:
        existing = db.query(GroupCard).filter(GroupCard.id == group_card_id).first()
        if not existing:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group card not found")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed to update this group card")

    return crud_group.update_group_card(db, group_card, updates)


@router.delete("/card/{group_card_id}")
def delete_group_card(
    group_card_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    group_card = crud_group.get_group_card_owned_by_leader(db, group_card_id, current_user.id)
    if not group_card:
        existing = db.query(GroupCard).filter(GroupCard.id == group_card_id).first()
        if not existing:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Group card not found")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed to delete this group card")

    crud_group.delete_group_card(db, group_card)
    return {"message": "Group card deleted successfully"}
