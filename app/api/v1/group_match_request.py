from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.group_match_request import GroupMatchRequest

router = APIRouter()



@router.post("/match-request/{request_id}/respond")
def respond_to_request(request_id: int, decision: str, db: Session = Depends(get_db)):
    if decision not in ["accepted", "rejected"]:
        raise HTTPException(status_code=400, detail="Invalid decision")

    req = db.query(GroupMatchRequest).filter_by(id=request_id).first()
    if not req:
        raise HTTPException(status_code=404, detail="Request not found")

    req.status = decision
    db.commit()
    return {"message": f"Request {decision}"}


@router.post("/match-request/{from_group_id}/{to_group_id}")
def send_match_request(from_group_id: int, to_group_id: int, db: Session = Depends(get_db)):
    existing = db.query(GroupMatchRequest).filter_by(
        from_group_id=from_group_id,
        to_group_id=to_group_id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Request already exists")

    request = GroupMatchRequest(from_group_id=from_group_id, to_group_id=to_group_id)
    db.add(request)
    db.commit()
    db.refresh(request)
    return {"message": "Match request sent"}

