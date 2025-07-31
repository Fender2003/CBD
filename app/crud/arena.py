from sqlalchemy.orm import Session
from uuid import UUID

from app.db.models.arena import Arena
from app.db.models.ArenaHourlyPrice import ArenaHourlyPrice
from app.schemas.arena import ArenaCreate
from app.schemas.arena_hourly_price import ArenaHourlyPriceCreate

# ---------------- Arena ----------------
def create_arena(db: Session, arena: ArenaCreate) -> Arena:
    db_arena = Arena(**arena.dict())
    db.add(db_arena)
    db.commit()
    db.refresh(db_arena)
    return db_arena

# ---------------- Arena Hourly Price ----------------
def create_arena_hourly_price(db: Session, data: ArenaHourlyPriceCreate) -> ArenaHourlyPrice:
    db_price = ArenaHourlyPrice(**data.dict())
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price

def get_arena_hourly_prices(db: Session, arena_id: UUID) -> list[ArenaHourlyPrice]:
    return db.query(ArenaHourlyPrice).filter_by(arena_id=arena_id).all()
