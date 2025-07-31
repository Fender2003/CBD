from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.arena import ArenaCreate, ArenaOut
from app.schemas.arena_hourly_price import ArenaHourlyPriceCreate, ArenaHourlyPriceResponse

from app.crud.arena import create_arena
from app.db.models.ArenaHourlyPrice import ArenaHourlyPrice

from app.db.session import get_db

router = APIRouter()

# -------------------- Arena --------------------
@router.post("/add-arena", response_model=ArenaOut)
def add_arena(arena: ArenaCreate, db: Session = Depends(get_db)):
    return create_arena(db, arena)

# -------------------- Arena Hourly Price --------------------
@router.post("/add-hourly-price", response_model=ArenaHourlyPriceResponse)
def add_hourly_price(price_data: ArenaHourlyPriceCreate, db: Session = Depends(get_db)):
    price = ArenaHourlyPrice(**price_data.dict())
    db.add(price)
    db.commit()
    db.refresh(price)
    return price

@router.get("/hourly-prices/{arena_id}", response_model=list[ArenaHourlyPriceResponse])
def get_hourly_prices(arena_id: UUID, db: Session = Depends(get_db)):
    return db.query(ArenaHourlyPrice).filter_by(arena_id=arena_id).all()
