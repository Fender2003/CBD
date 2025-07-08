from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.group import GroupCreate, GroupCardCreate
from app.schemas.group_out import GroupOut, GroupCardOut
from app.db.session import get_db
from app.crud import group as crud_group

router = APIRouter()

@router.post("/create", response_model=GroupOut)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    return crud_group.create_group(db, group.match_type, group.name, group.leader_id, group.friend_phone_numbers)

@router.post("/card", response_model=GroupCardOut)
def create_group_card(data: GroupCardCreate, db: Session = Depends(get_db)):
    return crud_group.create_group_card(db, data.group_id, data.start_time, data.end_time, data.booking_date, data.court)
