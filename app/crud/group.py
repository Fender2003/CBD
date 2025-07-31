from sqlalchemy.orm import Session
from app.db.models.group import Group
from app.db.models.group_player import GroupPlayer
from app.db.models.group_card import GroupCard
from app.db.models.user import User
from app.utils.geo_matrix import get_coordinates 
import json
from datetime import date, time
import uuid

def create_group(db: Session, match_type: str, name: str, leader_id: str, phone_numbers: list):
    if match_type not in ["singles", "doubles"]:
        raise ValueError("match_type must be 'singles' or 'doubles'")

    if match_type == "singles":
        if len(phone_numbers) >= 1:
            raise ValueError("Singles match must have only one friend.")
    elif match_type == "doubles":
        if len(phone_numbers) >= 3:
            raise ValueError("Doubles match must have exactly three friends.")

    group = Group(name=name, leader_id=leader_id, match_type=match_type)
    db.add(group)
    db.commit()
    db.refresh(group)

    all_members = []

    if match_type == "singles":
        leader = db.query(User).get(leader_id)
        all_members = [leader]
    else:
        all_members = db.query(User).filter(User.phone_number.in_(phone_numbers)).all()
        leader = db.query(User).get(leader_id)
        if leader not in all_members:
            all_members.append(leader)

        if len(all_members) > 4:
            raise ValueError("Maximum 4 players allowed in a doubles match.")

    for member in all_members:
        db.add(GroupPlayer(group_id=group.id, user_id=member.id))

    db.commit()
    return group

def create_group_card(
    db: Session,
    group_id: int,
    start_time: time,
    end_time: time,
    booking_date: date,
    arena_id: uuid,
    rated: bool,
):
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise ValueError("Group not found.")

    match_type = group.match_type.lower()

    players = db.query(GroupPlayer).filter(GroupPlayer.group_id == group_id).all()
    player_ids = [p.user_id for p in players]
    player_objs = db.query(User).filter(User.id.in_(player_ids)).all()

    if not player_objs:
        return None

    # Initialize defaults
    avg_age = None
    gender_combo = ""
    coords = []
    player_count = len(player_objs)

    if match_type == "singles":
        # Only use the group leader's info
        leader = db.query(User).filter(User.id == group.leader_id).first()
        if not leader:
            return None

        avg_age = leader.age
        gender_combo = leader.gender[0].lower()
        full_address = f"{leader.address}, {leader.city}, {leader.state}"
        latlng = get_coordinates(full_address)
        coords = [latlng] if latlng else []
        player_count = 1

    elif match_type == "doubles":
        avg_age = int(sum(p.age for p in player_objs) / len(player_objs))
        genders = [p.gender.lower() for p in player_objs]
        gender_combo = "".join(sorted([g[0] for g in genders]))

        for player in player_objs:
            full_address = f"{player.address}, {player.city}, {player.state}"
            latlng = get_coordinates(full_address)
            if latlng:
                coords.append(latlng)

    else:
        raise ValueError("Invalid match type. Must be 'singles' or 'doubles'.")

    centroid = None
    if coords:
        lats = [lat for lat, _ in coords]
        lngs = [lng for _, lng in coords]
        centroid = {
            "lat": round(sum(lats) / len(lats), 6),
            "lng": round(sum(lngs) / len(lngs), 6)
        }

    group_card = GroupCard(
        group_id=group_id,
        average_age=avg_age,
        gender_combo=gender_combo,
        centroid=json.dumps(centroid) if centroid else None,
        start_time=start_time,
        end_time=end_time,
        booking_date=booking_date,
        player_count=player_count,
        arena_id=arena_id,
        rated=rated,
    )

    db.add(group_card)
    db.commit()
    db.refresh(group_card)
    return group_card
