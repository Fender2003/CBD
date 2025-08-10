from geopy.distance import geodesic
from datetime import datetime
import json
import math
from geopy.distance import geodesic
from app.db.models.arena import Arena

def calculate_priority_score(g1, g2, db):
    score = 0
    primary = 0
    secondary = 0
    if(not g2['is_in_lobby']):
        return 0,0,0
    
    # --- PRIMARY FACTORS ---
    # 1. Match Type
    if g1["match_type"] == g2["match_type"]:
        primary += 0.1


    # 2. Booking Date
    if g1["booking_date"] == g2["booking_date"]:
        primary += 0.20

    # 3. Start Time Similarity
    time_fmt = "%H:%M:%S"
    s1 = datetime.strptime(g1["start_time"], time_fmt).time()
    s2 = datetime.strptime(g2["start_time"], time_fmt).time()
    diff_minutes = abs((s1.hour * 60 + s1.minute) - (s2.hour * 60 + s2.minute))
    time_score = max(0, 1 - (diff_minutes / 60))
    primary += 0.20 * time_score

    # 4. Arena Match
    arena_score = 0.0
    arena1 = db.query(Arena).filter(Arena.id == g1["arena_id"]).first()
    arena2 = db.query(Arena).filter(Arena.id == g2["arena_id"]).first()
    if arena1 and arena2:
        coord1 = arena1.location_coordinates
        coord2 = arena2.location_coordinates

        distance_km = geodesic(
            (coord1["latitude"], coord1["longitude"]),
            (coord2["latitude"], coord2["longitude"])
        ).km

        # Exponential decay scoring (0 to 0.2 range)
        k = 0.6
        arena_score = 0.15 * math.exp(-k * distance_km)
    else:
        print("no courts dafod!")

    primary += arena_score


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

    # 8. Player count matching (for doubles)
    if g1["match_type"] == "doubles":
        if g1["player_count"] + g2["player_count"] == 4:
            secondary += 0.05
    if g1["match_type"] == "singles":
        if g1["player_count"] + g2["player_count"] == 2:
            secondary += 0.05

    total_score = round(primary + secondary, 3)

    print(primary, secondary, total_score)
    return total_score, round(primary, 3), round(secondary, 3)
