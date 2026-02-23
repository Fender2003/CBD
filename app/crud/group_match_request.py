from uuid import UUID

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session, aliased

from app.db.models.group import Group
from app.db.models.group_card import GroupCard
from app.db.models.group_match_request import GroupMatchRequest


def get_group_card(db: Session, group_card_id: UUID) -> GroupCard | None:
    return db.query(GroupCard).filter(GroupCard.id == group_card_id).first()


def get_group(db: Session, group_id: UUID) -> Group | None:
    return db.query(Group).filter(Group.id == group_id).first()


def get_active_pending_request_between_cards(
    db: Session, from_group_card_id: UUID, to_group_card_id: UUID
) -> GroupMatchRequest | None:
    return (
        db.query(GroupMatchRequest)
        .filter(
            GroupMatchRequest.status == "pending",
            or_(
                and_(
                    GroupMatchRequest.from_group_id == from_group_card_id,
                    GroupMatchRequest.to_group_id == to_group_card_id,
                ),
                and_(
                    GroupMatchRequest.from_group_id == to_group_card_id,
                    GroupMatchRequest.to_group_id == from_group_card_id,
                ),
            ),
        )
        .first()
    )


def create_match_request(db: Session, from_group_card_id: UUID, to_group_card_id: UUID) -> GroupMatchRequest:
    req = GroupMatchRequest(from_group_id=from_group_card_id, to_group_id=to_group_card_id)
    db.add(req)
    db.commit()
    db.refresh(req)
    return req


def get_match_request(db: Session, request_id: UUID) -> GroupMatchRequest | None:
    return db.query(GroupMatchRequest).filter(GroupMatchRequest.id == request_id).first()


def list_pending_for_target_owner(db: Session, owner_id: UUID):
    from_card = aliased(GroupCard)
    to_card = aliased(GroupCard)
    from_group = aliased(Group)
    to_group = aliased(Group)

    rows = (
        db.query(GroupMatchRequest, from_card, to_card, from_group)
        .join(from_card, GroupMatchRequest.from_group_id == from_card.id)
        .join(to_card, GroupMatchRequest.to_group_id == to_card.id)
        .join(from_group, from_card.group_id == from_group.id)
        .join(to_group, to_card.group_id == to_group.id)
        .filter(GroupMatchRequest.status == "pending", to_group.leader_id == owner_id)
        .order_by(GroupMatchRequest.timestamp.desc())
        .all()
    )

    return [
        {
            "request_id": req.id,
            "from_group_card_id": from_gc.id,
            "to_group_card_id": to_gc.id,
            "from_group_name": from_g.name,
            "booking_date": to_gc.booking_date,
            "start_time": to_gc.start_time,
            "end_time": to_gc.end_time,
            "arena_id": to_gc.arena_id,
            "status": req.status,
            "timestamp": req.timestamp,
        }
        for req, from_gc, to_gc, from_g in rows
    ]
