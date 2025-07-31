from geopy.distance import geodesic

def calculate_match_score_with_arena_distance(group1, group2, db):
    score = 0

    # Example rules for match_type, gender_combo, etc. (same as before)
    if group1.match_type == group2.match_type:
        score += 10
    if group1.gender_combo == group2.gender_combo:
        score += 10

    # Add more rules as needed...

    # Get arena locations from the Arena table
    from app.db.models.arena import Arena  # Make sure import is correct

    arena1 = db.query(Arena).filter(Arena.id == group1.arena_id).first()
    arena2 = db.query(Arena).filter(Arena.id == group2.arena_id).first()

    if arena1 and arena2:
        coord1 = arena1.location_coordinates  # {"latitude": ..., "longitude": ...}
        coord2 = arena2.location_coordinates

        # Calculate distance in km
        distance_km = geodesic(
            (coord1["latitude"], coord1["longitude"]),
            (coord2["latitude"], coord2["longitude"])
        ).km

        # Score based on proximity (closer = higher score)
        if distance_km < 1:
            score += 15
        elif distance_km < 3:
            score += 10
        elif distance_km < 5:
            score += 5
        else:
            score += 0  # too far

    return score
