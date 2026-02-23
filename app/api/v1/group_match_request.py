from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from uuid import UUID
from app.core.dependencies import get_current_user
from app.db.models.user import User
from app.schemas.group_match_request import MatchRequestActionResponse, MatchRequestPendingOut
from app.crud import group_match_request as crud_gmr

router = APIRouter()


@router.post("/match-request/{from_group_card_id}/{to_group_card_id}")
def send_match_request(
    from_group_card_id: UUID,
    to_group_card_id: UUID,
    force: bool = Query(False),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    if from_group_card_id == to_group_card_id:
        raise HTTPException(status_code=400, detail="Cannot send request to the same group")

    existing = crud_gmr.get_active_pending_request_between_cards(db, from_group_card_id, to_group_card_id)
    if existing:
        raise HTTPException(status_code=400, detail="An active request already exists between these groups")

    from_card = crud_gmr.get_group_card(db, from_group_card_id)
    to_card = crud_gmr.get_group_card(db, to_group_card_id)

    if not from_card or not to_card:
        raise HTTPException(status_code=404, detail="Group card not found")

    from_group = crud_gmr.get_group(db, from_card.group_id)
    to_group = crud_gmr.get_group(db, to_card.group_id)

    if not from_group or not to_group:
        raise HTTPException(status_code=404, detail="Group not found")

    if from_group.leader_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed to send request from this group")

    mismatches = []

    if from_card.arena_id != to_card.arena_id:
        mismatches.append("Arena mismatch")
    if from_card.booking_date != to_card.booking_date:
        mismatches.append("Booking date mismatch")
    if from_card.start_time != to_card.start_time or from_card.end_time != to_card.end_time:
        mismatches.append("Time slot mismatch")
    if not (from_card.is_in_lobby and to_card.is_in_lobby):
        mismatches.append("Both groups are not currently in lobby")

    total_players = (from_card.player_count or 0) + (to_card.player_count or 0)

    if from_group.match_type != to_group.match_type:
        mismatches.append("Match type mismatch")

    if from_group.match_type == "doubles" and total_players != 4:
        mismatches.append(f"Total players for doubles is {total_players}, expected 4")
    elif from_group.match_type == "singles" and total_players != 2:
        mismatches.append(f"Total players for singles is {total_players}, expected 2")

    if mismatches and not force:
        return {
            "message": "Mismatch detected. Confirm to proceed anyway.",
            "requires_confirmation": True,
            "mismatches": mismatches,
        }

    request = crud_gmr.create_match_request(db, from_group_card_id, to_group_card_id)

    return {
        "message": "Match request sent",
        "request_id": request.id,
        "mismatch_warning": mismatches,
    }


@router.get("/match-request/pending", response_model=list[MatchRequestPendingOut])
def get_pending_match_requests(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud_gmr.list_pending_for_target_owner(db, current_user.id)


@router.post("/respond/{request_id}", response_model=MatchRequestActionResponse)
def respond_to_match_request(
    request_id: UUID,
    decision: str = Query(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    decision = decision.lower()
    if decision not in ["accepted", "rejected"]:
        raise HTTPException(status_code=400, detail="Invalid decision")

    match_request = crud_gmr.get_match_request(db, request_id)
    if not match_request:
        raise HTTPException(status_code=404, detail="Match request not found")

    if match_request.status != "pending":
        raise HTTPException(status_code=400, detail="Only pending requests can be responded to")

    to_card = crud_gmr.get_group_card(db, match_request.to_group_id)
    if not to_card:
        raise HTTPException(status_code=404, detail="Target group card not found")

    to_group = crud_gmr.get_group(db, to_card.group_id)
    if not to_group or to_group.leader_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed to respond to this request")

    match_request.status = decision
    db.commit()

    return {"message": f"Match request {decision} successfully."}


@router.delete("/match-request/{request_id}/withdraw", response_model=MatchRequestActionResponse)
def withdraw_match_request(
    request_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    req = crud_gmr.get_match_request(db, request_id)

    if not req:
        raise HTTPException(status_code=404, detail="Request not found")

    from_card = crud_gmr.get_group_card(db, req.from_group_id)
    from_group = crud_gmr.get_group(db, from_card.group_id) if from_card else None

    if not from_group or from_group.leader_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed to withdraw this request")

    if req.status != "pending":
        raise HTTPException(status_code=400, detail="Cannot withdraw a request that is already matched or rejected")

    db.delete(req)
    db.commit()

    return {"message": "Match request withdrawn successfully"}
