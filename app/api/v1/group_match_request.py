from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.group_match_request import GroupMatchRequest
from uuid import UUID

router = APIRouter()


@router.post("/match-request/{from_group_card_id}/{to_group_card_id}")
def send_match_request(from_group_card_id: UUID, to_group_card_id: UUID, db: Session = Depends(get_db)):
    existing = db.query(GroupMatchRequest).filter_by(
        from_group_id=from_group_card_id,
        to_group_id=to_group_card_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Request already exists")

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
