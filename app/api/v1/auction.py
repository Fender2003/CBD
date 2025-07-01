from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import auction as schemas
from app.crud import auction as crud
from app.db.session import get_db

router = APIRouter()

# Create time auction
@router.post("/auction/time/initiate")
def start_time_auction(data: schemas.TimeAuctionCreate, db: Session = Depends(get_db)):
    return crud.create_time_auction(db, data.group1_id, data.group2_id)

# Select time
@router.post("/auction/time/select")
def select_time(data: schemas.TimeAuctionSelect, db: Session = Depends(get_db)):
    result = crud.select_time_slot(db, data.auction_id, data.group_id, data.slot)
    if not result:
        raise HTTPException(status_code=404, detail="Auction not found or invalid group")
    return result

# Polling endpoint
@router.get("/auction/time/status/{auction_id}")
def time_status(auction_id: int, db: Session = Depends(get_db)):
    result = crud.get_time_auction_status(db, auction_id)
    if not result:
        raise HTTPException(status_code=404, detail="Auction not found")
    return result


# Court auction endpoints
@router.post("/auction/court/initiate")
def start_court_auction(data: schemas.CourtAuctionCreate, db: Session = Depends(get_db)):
    return crud.create_court_auction(db, data.group1_id, data.group2_id)

@router.post("/auction/court/select")
def select_court(data: schemas.CourtAuctionSelect, db: Session = Depends(get_db)):
    result = crud.select_court(db, data.auction_id, data.group_id, data.court_name)
    if not result:
        raise HTTPException(status_code=404, detail="Auction not found or invalid group")
    return result

@router.get("/auction/court/status/{auction_id}")
def court_status(auction_id: int, db: Session = Depends(get_db)):
    result = crud.get_court_auction_status(db, auction_id)
    if not result:
        raise HTTPException(status_code=404, detail="Auction not found")
    return result
