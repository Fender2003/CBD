# utils/geo.py
import requests

API_KEY = "tx9ndK9SI3VlhQNdF8p1btlxliGYkXuctFlB7quAGxfjLwKa9I7Pa5z377nSANbt"

def get_coordinates(address: str) -> tuple[float, float] | None:
    url = "https://api.distancematrix.ai/maps/api/geocode/json"
    params = {"address": address, "key": API_KEY}

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("status") == "OK" and data.get("result"):
            location = data["result"][0]["geometry"]["location"]
            return location['lat'], location['lng']
    except Exception as e:
        print(f"Failed to get coordinates for {address}: {e}")
    
    return None
