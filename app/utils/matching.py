import json
from datetime import datetime
from geopy.distance import geodesic

def time_overlap_minutes(start1, end1, start2, end2):
    latest_start = max(start1, start2)
    earliest_end = min(end1, end2)
    delta = (earliest_end - latest_start).total_seconds() / 60
    return max(0, delta)

def calculate_match_score(g1, g2):
    try:
        c1 = json.loads(g1["centroid"])
        c2 = json.loads(g2["centroid"])
    except Exception:
        return 0

    pcount = g1["player_count"] + g2["player_count"]
    if pcount != 4:
        return 0

    age_diff = abs(g1["average_age"] - g2["average_age"])
    age_score = max(0, 1 - (age_diff / 40))

    date_score = 1.0 if g1["booking_date"] == g2["booking_date"] else 0.0

    fmt = "%H:%M:%S.%f"
    s1, e1 = datetime.strptime(g1["start_time"], fmt), datetime.strptime(g1["end_time"], fmt)
    s2, e2 = datetime.strptime(g2["start_time"], fmt), datetime.strptime(g2["end_time"], fmt)
    overlap = time_overlap_minutes(s1, e1, s2, e2)
    time_score = min(overlap / 60, 1.0)

    gender_combo = g1["gender_combo"] + g2["gender_combo"]
    solo_girl_flag = (gender_combo.count("f") == 1)
    gender_score = 0.5 if solo_girl_flag else 1.0

    group_distance = geodesic((c1["lat"], c1["lng"]), (c2["lat"], c2["lng"])).km
    distance_score = max(0, 1 - (group_distance / 10))

    score = (
        0.30 * age_score +
        0.25 * date_score +
        0.20 * time_score +
        0.15 * gender_score +
        0.10 * distance_score
    )

    return round(score, 3)

def rank_courts_by_proximity(courts, g1, g2):
    c1 = json.loads(g1["centroid"])
    c2 = json.loads(g2["centroid"])

    results = []
    for name, coords in courts.items():
        court_location = (coords[0], coords[1])
        dist1 = geodesic((c1["lat"], c1["lng"]), court_location).km
        dist2 = geodesic((c2["lat"], c2["lng"]), court_location).km
        avg_dist = (dist1 + dist2) / 2

        results.append({
            "court": name,
            "distance_from_g1_km": round(dist1, 2),
            "distance_from_g2_km": round(dist2, 2),
            "average_distance_km": round(avg_dist, 2)
        })

    results.sort(key=lambda x: x["average_distance_km"])
    return results
