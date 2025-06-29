from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.group_card import GroupCard
from app.utils.matching import calculate_match_score
import json

router = APIRouter()

@router.get("/match/{group_id}")
def get_matching_groups(group_id: int, db: Session = Depends(get_db)):
    current_group = db.query(GroupCard).filter(GroupCard.group_id == group_id).first()
    if not current_group:
        raise HTTPException(status_code=404, detail="Group not found")

    all_groups = db.query(GroupCard).filter(GroupCard.group_id != group_id).all()
    current_data = groupcard_to_dict(current_group)

    results = []
    for g in all_groups:
        other_data = groupcard_to_dict(g)
        score = calculate_match_score(current_data, other_data)
        if score > 0:
            results.append({
                "group_id": g.group_id,
                "match_score": score
            })

    sorted_results = sorted(results, key=lambda x: x["match_score"], reverse=True)
    return {"matches": sorted_results}



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
        "player_count": g.player_count
    }


@router.get("/best_courts/{group1_id}/{group2_id}")
def get_best_courts(group1_id: int, group2_id: int, db: Session = Depends(get_db)):
    from app.utils.matching import rank_courts_by_proximity

    # Load groups
    g1 = db.query(GroupCard).filter(GroupCard.group_id == group1_id).first()
    g2 = db.query(GroupCard).filter(GroupCard.group_id == group2_id).first()

    if not g1 or not g2:
        raise HTTPException(status_code=404, detail="One or both groups not found")

    # Load court coordinates
    try:
        with open("app/vadodara_courts.json", "r") as f:
            court_coords = json.load(f)
    except Exception:
        raise HTTPException(status_code=500, detail="Court data not available")

    g1_data = groupcard_to_dict(g1)
    g2_data = groupcard_to_dict(g2)

    ranked = rank_courts_by_proximity(court_coords, g1_data, g2_data)
    return {"ranked_courts": ranked}
