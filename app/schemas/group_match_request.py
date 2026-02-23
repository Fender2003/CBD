from pydantic import BaseModel
from datetime import datetime, date, time
from uuid import UUID


class GroupMatchRequestBase(BaseModel):
    from_group_id: UUID
    to_group_id: UUID


class GroupMatchRequestCreate(GroupMatchRequestBase):
    pass


class GroupMatchRequestOut(GroupMatchRequestBase):
    id: UUID
    from_group_id: UUID
    to_group_id: UUID
    status: str
    timestamp: datetime

    class Config:
        from_attributes = True


class MatchRequestCreateResponse(BaseModel):
    message: str
    request_id: UUID


class MatchRequestPendingOut(BaseModel):
    request_id: UUID
    from_group_card_id: UUID
    to_group_card_id: UUID
    from_group_name: str | None = None
    booking_date: date | None = None
    start_time: time | None = None
    end_time: time | None = None
    arena_id: UUID | None = None
    status: str
    timestamp: datetime


class MatchRequestActionResponse(BaseModel):
    message: str
