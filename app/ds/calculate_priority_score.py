from geopy.distance import geodesic
from datetime import datetime
import json
import app.ds.calculate_match_score_with_arena_distance as calculate_match_score_with_arena_distance
def calculate_priority_score(g1, g2):
    score = 0
    primary = 0
    secondary = 0

    # --- PRIMARY FACTORS ---
    # 1. Match Type
    if g1["match_type"] == g2["match_type"]:
        primary += 0.05

    # 2. Booking Date
    if g1["booking_date"] == g2["booking_date"]:
        primary += 0.25

    # 3. Start Time Similarity
    time_fmt = "%H:%M:%S"
    s1 = datetime.strptime(g1["start_time"], time_fmt).time()
    s2 = datetime.strptime(g2["start_time"], time_fmt).time()
    diff_minutes = abs((s1.hour * 60 + s1.minute) - (s2.hour * 60 + s2.minute))
    time_score = max(0, 1 - (diff_minutes / 60))
    primary += 0.25 * time_score

    # 4. Arena Match
    if g1["arena_id"] == g2["arena_id"]:
        primary += 0.2

    # 5. Rated Match
    if g1["rated"] and g2["rated"]:
        primary += 0.1

    # --- SECONDARY FACTORS ---
    # 6. Age Similarity
    age_diff = abs(g1["average_age"] - g2["average_age"])
    secondary += 0.1 * max(0, 1 - (age_diff / 40))

    # 7. Gender Combo
    gender_combo = g1["gender_combo"] + g2["gender_combo"]
    solo_girl_flag = gender_combo.count("f") == 1
    secondary += 0.05 if solo_girl_flag else 0.1

    # 8. Distance between arenas (based on arena's `location_coordinates`)
    try:
        loc1 = json.loads(g1["arena_location_coordinates"])
        loc2 = json.loads(g2["arena_location_coordinates"])
        latlon1 = (loc1["latitude"], loc1["longitude"])
        latlon2 = (loc2["latitude"], loc2["longitude"])
        arena_distance_km = geodesic(latlon1, latlon2).km
        distance_score = max(0, 1 - (arena_distance_km / 10))  # Full score if within 0 km, 0 score if >10 km
        secondary += 0.1 * distance_score
    except Exception:
        pass  # silently ignore distance errors

    # 9. Player count matching (for doubles)
    if g1["match_type"] == "doubles":
        if g1["player_count"] + g2["player_count"] == 4:
            secondary += 0.05

    total_score = round(primary + secondary, 3)
    return total_score, round(primary, 3), round(secondary, 3)
