from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.crud import group as crud_group
from app.db.models.user import User
from app.db.session import get_db
from app.schemas.challenge_team import ChallengeTeamLobbyOut

router = APIRouter()


@router.get("/challenge-team/lobby", response_model=list[ChallengeTeamLobbyOut])
def get_challenge_lobby(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    _ = current_user
    return crud_group.get_challenge_lobby_group_cards(db)


@router.get("/challenge-team/my-lobby", response_model=list[ChallengeTeamLobbyOut])
def get_my_challenge_lobby(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud_group.get_challenge_lobby_group_cards(db, leader_id=current_user.id)
