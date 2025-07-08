from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.group_card import GroupCard
from app.utils.matching import calculate_match_score
import json

router = APIRouter()

from datetime import datetime
from geopy.distance import geodesic
import json

def calculate_priority_score(g1, g2):
    # Match Type must be the same
    if g1["match_type"] != g2["match_type"]:
        return 0

    # Load centroids
    try:
        c1 = json.loads(g1["centroid"])
        c2 = json.loads(g2["centroid"])
    except Exception:
        return 0

    # Player Count Check (optional, you can remove if unnecessary)
    pcount = g1["player_count"] + g2["player_count"]
    if g1["match_type"] == "doubles" and pcount != 4:
        return 0

    # --- Score Components ---
    score = 0

    # 1. Booking Date (weight: 0.25)
    date_score = 1.0 if g1["booking_date"] == g2["booking_date"] else 0.0
    score += 0.25 * date_score

    # 2. Start Time Similarity (weight: 0.25)
    time_fmt = "%H:%M:%S.%f"
    s1 = datetime.strptime(g1["start_time"], time_fmt).time()
    s2 = datetime.strptime(g2["start_time"], time_fmt).time()

    # Convert to minutes since midnight
    def to_minutes(t): return t.hour * 60 + t.minute
    diff_minutes = abs(to_minutes(s1) - to_minutes(s2))
    time_score = max(0, 1 - (diff_minutes / 60))  # full score if exact, 0 if > 60 mins
    score += 0.25 * time_score

    # 3. Court Match (weight: 0.2)
    court_score = 1.0 if g1["court"] == g2["court"] else 0.0
    score += 0.2 * court_score

    # 4. Age Similarity (weight: 0.1)
    age_diff = abs(g1["average_age"] - g2["average_age"])
    age_score = max(0, 1 - (age_diff / 40))
    score += 0.1 * age_score

    # 5. Gender Combo Balance (weight: 0.1)
    gender_combo = g1["gender_combo"] + g2["gender_combo"]
    solo_girl_flag = (gender_combo.count("f") == 1)
    gender_score = 0.5 if solo_girl_flag else 1.0
    score += 0.1 * gender_score

    # 6. Distance Score (weight: 0.1)
    group_distance = geodesic((c1["lat"], c1["lng"]), (c2["lat"], c2["lng"])).km
    distance_score = max(0, 1 - (group_distance / 10))  # full score if <1km, 0 if >10km
    score += 0.1 * distance_score

    return round(score, 3)


def groupcard_to_dict(g):
    return {
        "id": g.id,
        "group_id": g.group_id,
        "average_age": g.average_age,
        "gender_combo": g.gender_combo,
        "centroid": g.centroid,
        "start_time": str(g.start_time),
        "end_time": str(g.end_time),
        "booking_date": str(g.booking_date),
        "player_count": g.player_count,
        "match_type": g.group.match_type,
        "court": g.court
    }



@router.get("/smart_match/{group_id}")
def smart_match(group_id: int, db: Session = Depends(get_db)):
    current_group = db.query(GroupCard).filter(GroupCard.group_id == group_id).first()
    if not current_group:
        raise HTTPException(status_code=404, detail="Group not found")

    all_groups = db.query(GroupCard).filter(GroupCard.group_id != group_id).all()
    current_data = groupcard_to_dict(current_group)

    results = []
    for g in all_groups:
        other_data = groupcard_to_dict(g)
        score = calculate_priority_score(current_data, other_data)
        if score > 0:
            results.append({
                "group_id": g.group_id,
                "match_score": score
            })

    sorted_results = sorted(results, key=lambda x: x["match_score"], reverse=True)
    return {"matches": sorted_results}


