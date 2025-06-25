g2 = {
  "id": 4,
  "group_id": 6,
  "average_age": 21,
  "gender_combo": "mm",
  "centroid": "{\"lat\": 22.330501, \"lng\": 73.192204}",
  "start_time": "18:00:00.449000",
  "end_time": "21:00:45.449000",
  "booking_date": "2025-06-26",
  "player_count": 2
}

g1 = {
  "id": 3,
  "group_id": 5,
  "average_age": 26,
  "gender_combo": "ff",
  "centroid": "{\"lat\": 22.396831, \"lng\": 73.191412}",
  "start_time": "16:00:00.449",
  "end_time": "22:00:45.449",
  "booking_date": "2025-06-26",
  "player_count": 2
}


import json
from datetime import datetime, timedelta
from geopy.distance import geodesic

def time_overlap_minutes(start1, end1, start2, end2):
    latest_start = max(start1, start2)
    earliest_end = min(end1, end2)
    delta = (earliest_end - latest_start).total_seconds() / 60
    return max(0, delta)

def calculate_match_score(g1, g2, court_coords_dict):

    c1 = json.loads(g1["centroid"])
    c2 = json.loads(g2["centroid"])

    pcount = g1["player_count"] + g2["player_count"]
    if pcount != 4:
        return 0

    # Age score
    age_diff = abs(g1["average_age"] - g2["average_age"])
    age_score = max(0, 1 - (age_diff / 40))  # assume 20 yrs difference max

    # Date score
    date_score = 1.0 if g1["booking_date"] == g2["booking_date"] else 0.0

    # 3. Time score
    fmt = "%H:%M:%S.%f"
    s1, e1 = datetime.strptime(g1["start_time"], fmt), datetime.strptime(g1["end_time"], fmt)
    s2, e2 = datetime.strptime(g2["start_time"], fmt), datetime.strptime(g2["end_time"], fmt)
    overlap = time_overlap_minutes(s1, e1, s2, e2)
    time_score = min(overlap / 60, 1.0)

    # 4. Gender logic
    gender_combo = g1["gender_combo"] + g2["gender_combo"]
    solo_girl_flag = (gender_combo.count("f") == 1)
    gender_score = 0.5 if solo_girl_flag else 1.0

    # 5. Distance score (find closest midpoint court and scale)
    group_distance = geodesic((c1["lat"], c1["lng"]), (c2["lat"], c2["lng"])).km
    distance_score = max(0, 1 - (group_distance / 10))  # scale: if >10 km, score drops

    # Final weighted score
    score = (
        0.30 * age_score +
        0.25 * date_score +
        0.20 * time_score +
        0.15 * gender_score +
        0.10 * distance_score
    )

    return round(score, 3)
import json


with open('app/vadodara_courts.json', 'r') as file:
    court_coords_dict = json.load(file)

score = calculate_match_score(g1, g2, court_coords_dict)
print("Score between g1 and g2:", score)
