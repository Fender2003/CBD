# import requests

# API_KEY = "8AUwEJfTl9Bd3CPAPzAij4r8t7Kblif1A3C9MwxDSLKdN1r9IsHlpgzMPiuQ52xJ" 

# # origins = ["Sardar Nagar, Nizampura, Vadodara, Gujarat, India"]
# # destinations = ["Amitnagar Circle, Vadodara, India"]
# origins = ["22.3251,73.1811"]
# destinations = ["22.3108,73.2126"]

# def get_distances(origins, destinations, key):
#     base_url = "https://api.distancematrix.ai/maps/api/distancematrix/json"
    
#     params = {
#         "origins": "|".join(origins),
#         "destinations": "|".join(destinations),
#         "mode": "driving",
#         "traffic_model": "best_guess",
#         "departure_time": "now",
#         "key": key
#     }

#     response = requests.get(base_url, params=params)
#     if response.status_code != 200:
#         print("API Request failed:", response.status_code)
#         return

#     data = response.json()
#     print("Results:\n")

#     for i, origin in enumerate(origins):
#         for j, destination in enumerate(destinations):
#             el = data["rows"][i]["elements"][j]
#             if el["status"] == "OK":
#                 print(f"From {origin} to {destination}:")
#                 print(f"  Distance: {el['distance']['text']} ({el['distance']['value']} meters)")
#                 print(f"  Duration: {el['duration']['text']} ({el['duration']['value']} seconds)\n")
#             else:
#                 print(f"From {origin} to {destination}: {el['status']}")

# get_distances(origins, destinations, API_KEY)

