from datetime import date, datetime, time
from uuid import UUID

from pydantic import BaseModel


class ChallengeTeamLobbyOut(BaseModel):
    group_card_id: UUID
    group_id: UUID
    group_name: str | None = None
    match_type: str
    booking_date: date
    start_time: time
    end_time: time
    arena_id: UUID
    rated: bool
    player_count: int
    is_in_lobby: bool
    created_at: datetime | None = None
