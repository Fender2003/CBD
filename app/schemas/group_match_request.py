from pydantic import BaseModel
from datetime import datetime

class GroupMatchRequestBase(BaseModel):
    from_group_id: int
    to_group_id: int

class GroupMatchRequestCreate(GroupMatchRequestBase):
    pass

class GroupMatchRequestOut(GroupMatchRequestBase):
    id: int
    status: str
    timestamp: datetime

    class Config:
        orm_mode = True
