from pydantic import BaseModel
from datetime import datetime
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