from pydantic import BaseModel
from typing import Optional

class TimeAuctionCreate(BaseModel):
    group1_id: int
    group2_id: int

class TimeAuctionSelect(BaseModel):
    auction_id: int
    group_id: int
    slot: str

class CourtAuctionCreate(BaseModel):
    group1_id: int
    group2_id: int

class CourtAuctionSelect(BaseModel):
    auction_id: int
    group_id: int
    court_name: str
