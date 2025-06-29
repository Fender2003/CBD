# from geopy.distance import geodesic
# import json

# def rank_courts_by_proximity(courts, g1, g2):

#     c1 = json.loads(g1["centroid"])
#     c2 = json.loads(g2["centroid"])

#     results = []
#     for name, coords in courts.items():
#         court_location = (coords[0], coords[1])
#         dist1 = geodesic((c1["lat"], c1["lng"]), court_location).km
#         dist2 = geodesic((c2["lat"], c2["lng"]), court_location).km
#         avg_dist = (dist1 + dist2) / 2

#         results.append({
#             "court": name,
#             "distance_from_g1_km": round(dist1, 2),
#             "distance_from_g2_km": round(dist2, 2),
#             "average_distance_km": round(avg_dist, 2)
#         })

#     results.sort(key=lambda x: x["average_distance_km"])
#     return results

# g2 = {
#   "id": 4,
#   "group_id": 6,
#   "average_age": 21,
#   "gender_combo": "mm",
#   "centroid": "{\"lat\": 22.330501, \"lng\": 73.192204}",
#   "start_time": "18:00:00.449000",
#   "end_time": "21:00:45.449000",
#   "booking_date": "2025-06-26",
#   "player_count": 2
# }

# g1 = {
#   "id": 3,
#   "group_id": 5,
#   "average_age": 26,
#   "gender_combo": "ff",
#   "centroid": "{\"lat\": 22.396831, \"lng\": 73.191412}",
#   "start_time": "16:00:00.449",
#   "end_time": "22:00:45.449",
#   "booking_date": "2025-06-26",
#   "player_count": 2
# }


# with open('app/vadodara_courts.json', 'r') as file:
#     courts_dict = json.load(file)

# ranked_courts = rank_courts_by_proximity(courts_dict, g1, g2)

# for court in ranked_courts:
#     print(f"{court['court']}: Avg {court['average_distance_km']} km (g1: {court['distance_from_g1_km']}, g2: {court['distance_from_g2_km']})")
