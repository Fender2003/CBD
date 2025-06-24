import requests

API_KEY = "tx9ndK9SI3VlhQNdF8p1btlxliGYkXuctFlB7quAGxfjLwKa9I7Pa5z377nSANbt"
address = "Sardar Nagar, Nizampura, Vadodara, Gujarat, India"
def get_coordinates(address, key):
    base_url = "https://api.distancematrix.ai/maps/api/geocode/json"
    params = {
        "address": address,
        "key": key
    }
    response = requests.get(base_url, params=params)
    print("Raw Response:", response.status_code)
    data = response.json()
    # print("JSON:", data)

    if data.get("status") == "OK":
        location = data["result"][0]["geometry"]["location"]
        print(f"Coordainates of '{address}':")
        print(f"  Latitude: {location['lat']}")
        print(f"  Longitude: {location['lng']}")
        return location['lat'], location['lng']
    else:
        print("Geocoding failed:", data.get("status"), data.get("error_message"))

get_coordinates(address, API_KEY)
