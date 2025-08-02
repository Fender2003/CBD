from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.group_match_request import GroupMatchRequest
from uuid import UUID
from app.db.models.group_card import GroupCard
from app.db.models.group import Group

router = APIRouter()



@router.post("/match-request/{from_group_card_id}/{to_group_card_id}")
def send_match_request(from_group_card_id: UUID, to_group_card_id: UUID, db: Session = Depends(get_db)):

    existing = db.query(GroupMatchRequest).filter_by(
        from_group_id=from_group_card_id,
        to_group_id=to_group_card_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Request already exists")

    from_card = db.query(GroupCard).filter_by(id=from_group_card_id).first()
    to_card = db.query(GroupCard).filter_by(id=to_group_card_id).first()

    if not from_card or not to_card:
        raise HTTPException(status_code=404, detail="Group card not found")

    if from_card.arena_id != to_card.arena_id:
        raise HTTPException(status_code=400, detail="Arena mismatch")
    if from_card.booking_date != to_card.booking_date:
        raise HTTPException(status_code=400, detail="Booking date mismatch")
    if from_card.start_time != to_card.start_time or from_card.end_time != to_card.end_time:
        raise HTTPException(status_code=400, detail="Time slot mismatch")
    if not (from_card.is_in_lobby and to_card.is_in_lobby):
        raise HTTPException(status_code=400, detail="Both groups must be in the lobby")

    from_count = len(from_card.gender_combo)
    to_count = len(to_card.gender_combo)
    total_players = from_count + to_count

    # Get match type from Group model
    from_group = db.query(Group).filter_by(id=from_card.group_id).first()
    to_group = db.query(Group).filter_by(id=to_card.group_id).first()

    if not from_group or not to_group:
        raise HTTPException(status_code=404, detail="Group not found")

    if from_group.match_type != to_group.match_type:
        raise HTTPException(status_code=400, detail="Match type mismatch")

    # Player count warning logic
    if from_group.match_type == "doubles" and total_players != 4:
        raise HTTPException(status_code=400, detail=f"Total player count must be 4 for doubles, got {total_players}")
    elif from_group.match_type == "singles" and total_players != 2:
        raise HTTPException(status_code=400, detail=f"Total player count must be 2 for singles, got {total_players}")

    # Create request
    request = GroupMatchRequest(from_group_id=from_group_card_id, to_group_id=to_group_card_id)
    db.add(request)
    db.commit()
    db.refresh(request)

    return {"message": "Match request sent"}



@router.post("/respond/{request_id}")
def respond_to_match_request(
    request_id: UUID,
    decision: str = Query(...),
    db: Session = Depends(get_db),
):
    if decision not in ["accepted", "rejected"]:
        raise HTTPException(status_code=400, detail="Invalid decision")

    match_request = db.query(GroupMatchRequest).filter(GroupMatchRequest.id == request_id).first()

    if not match_request:
        raise HTTPException(status_code=404, detail="Match request not found")

    match_request.status = decision
    db.commit()

    return {"message": f"Match request {decision} successfully."}





@router.delete("/match-request/{request_id}/withdraw")
def withdraw_match_request(request_id: UUID, db: Session = Depends(get_db)):
    req = db.query(GroupMatchRequest).filter_by(id=request_id).first()

    if not req:
        raise HTTPException(status_code=404, detail="Request not found")

    if req.status != "pending":
        raise HTTPException(status_code=400, detail="Cannot withdraw a request that is already matched or rejected")

    db.delete(req)
    db.commit()

    return {"message": "Match request withdrawn successfully"}
