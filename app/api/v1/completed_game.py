# app/api/routes/completed_game.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import uuid4
from datetime import datetime

from app.db.session import get_db
from app.db.models.group_match_request import GroupMatchRequest
from app.db.models.completed_game import CompletedGame
from app.db.models.group_card import GroupCard
from app.db.models.group import Group
from app.db.models.ArenaHourlyPrice import ArenaHourlyPrice  


from app.schemas.completed_game import CompleteGameRequest

router = APIRouter()

@router.post("/games/complete")
def complete_game_from_match_request(payload: CompleteGameRequest, db: Session = Depends(get_db)):
    # 1. Get the match request
    match_request = db.query(GroupMatchRequest).filter(GroupMatchRequest.id == payload.match_req_id).first()
    if not match_request:
        raise HTTPException(status_code=404, detail="Match request not found")

    if match_request.status != "accepted":
        raise HTTPException(status_code=400, detail="Match request is not accepted")

    # 2. Get both group cards
    from_group = db.query(GroupCard).filter(GroupCard.id == match_request.from_group_id).first()
    to_group = db.query(GroupCard).filter(GroupCard.id == match_request.to_group_id).first()

    group = db.query(Group).filter(Group.id == from_group.group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group not found for from_group")

    hourly_prices = db.query(ArenaHourlyPrice).filter(ArenaHourlyPrice.arena_id == from_group.arena_id).all()

    matched_price = None
    for price_entry in hourly_prices:
        # Make sure the start and end times fall completely within a valid pricing block
        if (price_entry.start_hour <= from_group.start_time <= price_entry.end_hour and
            price_entry.start_hour <= from_group.end_time <= price_entry.end_hour):
            matched_price = price_entry.price
            break

    if matched_price is None:
        raise HTTPException(status_code=400, detail="No valid pricing found for the given time slot")


    if not from_group or not to_group:
        raise HTTPException(status_code=404, detail="One or both group cards not found")

    # 3. Use from_group's details for booking info
    completed_game = CompletedGame(
        id=uuid4(),
        match_req_id=payload.match_req_id,
        court_id=from_group.arena_id,        # Assuming court == arena for now
        sport_id="b7f423c2-9217-4690-a2b8-e25f2ef847c3",        # Replace with actual sport logic if needed
        groupcard1_id=from_group.id,
        groupcard2_id=to_group.id,
        start_time=from_group.start_time,
        end_time=from_group.end_time,
        bookibg_date=from_group.booking_date,
        price=matched_price,                            # Set actual pricing logic here
        match_type=group.match_type,                # Or infer from group/match data
        is_rated=from_group.rated,
        created_at=datetime.utcnow()
    )

    db.add(completed_game)
    db.commit()
    db.refresh(completed_game)

    return {
        "detail": "CompletedGame created successfully.",
        "completed_game_id": str(completed_game.id)
    }