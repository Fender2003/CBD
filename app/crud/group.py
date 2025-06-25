from sqlalchemy.orm import Session
from app.db.models.group import Group
from app.db.models.group_player import GroupPlayer
from app.db.models.group_card import GroupCard
from app.db.models.user import User
from app.utils.geo_matrix import get_coordinates 
import json
from datetime import date, time

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


def create_group_card(db: Session, group_id: int, start_time: time, end_time: time, booking_date: date):
    players = db.query(GroupPlayer).filter(GroupPlayer.group_id == group_id).all()
    player_ids = [p.user_id for p in players]
    player_objs = db.query(User).filter(User.id.in_(player_ids)).all()

    if not player_objs:
        return None

    avg_age = int(sum(p.age for p in player_objs) / len(player_objs))

    genders = [p.gender.lower() for p in player_objs]
    gender_combo = "".join(sorted([g[0] for g in genders]))

    player_count = len(player_objs)

    coords = []
    for player in player_objs:
        full_address = f"{player.address}, {player.city}, {player.state}"
        latlng = get_coordinates(full_address)
        if latlng:
            coords.append(latlng)

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
        player_count=player_count
    )

    db.add(group_card)
    db.commit()
    db.refresh(group_card)
    return group_card
