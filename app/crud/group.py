from sqlalchemy.orm import Session
from app.db.models.group import Group
from app.db.models.group_player import GroupPlayer
from app.db.models.group_card import GroupCard
from app.db.models.user import User

def create_group(db: Session, name: str, leader_id: str, phone_numbers: list):
    group = Group(name=name, leader_id=leader_id)
    db.add(group)
    db.commit()
    db.refresh(group)

    # Fetch all friends by phone number
    all_members = db.query(User).filter(User.phone_number.in_(phone_numbers)).all()

    # Fetch leader and add if not already in the list
    leader = db.query(User).get(leader_id)
    if leader not in all_members:
        all_members.append(leader)

    # Create GroupPlayer entries
    for member in all_members:
        db.add(GroupPlayer(group_id=group.id, user_id=member.id))

    db.commit()
    return group

def create_group_card(db: Session, group_id: int):
    players = db.query(GroupPlayer).filter(GroupPlayer.group_id == group_id).all()
    player_ids = [p.user_id for p in players]

    player_objs = db.query(User).filter(User.id.in_(player_ids)).all()

    if not player_objs:
        return None  # prevent division by zero

    avg_age = int(sum(p.age for p in player_objs) / len(player_objs))
    genders = [p.gender.lower() for p in player_objs]
    gender_combo = "".join(sorted([g[0] for g in genders]))

    group_card = GroupCard(
        group_id=group_id,
        average_age=avg_age,
        gender_combo=gender_combo,
        centroid=None  # You can calculate this later
    )

    db.add(group_card)
    db.commit()
    db.refresh(group_card)
    return group_card
