import requests
import json
API_KEY = "tx9ndK9SI3VlhQNdF8p1btlxliGYkXuctFlB7quAGxfjLwKa9I7Pa5z377nSANbt"
address = "Plot 19, Old Padra Rd, next to Sera Pizzeria, near Hanuman temple, JP Nagar, Sukrutinagar, Diwalipura, Vadodara, Gujarat 390015"
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
        # print(f"Coordainates of '{address}':")
        # print(f"  Latitude: {location['lat']}")
        # print(f"  Longitude: {location['lng']}")
        return location['lat'], location['lng']
    else:
        print("Geocoding failed:", data.get("status"), data.get("error_message"))

court_list = ["Plot 19, Old Padra Rd, next to Sera Pizzeria, near Hanuman temple, JP Nagar, Sukrutinagar, Diwalipura, Vadodara, Gujarat 390015",
              "Carnival pickle ball, opposite Krishna Park Society, near Sayid Vasna, Saiyed Vasna, Vadodara, Gujarat 390007",
              "849F+265, Sevasi, Vadodara, Khanpur, Gujarat 391101",
              "Smash, b, Fitness MMA, h Dojo, Vasna - Bhayli Main Rd, nr. Kalyan Party Plot, Krishnadham Society, Saiyed Vasna, Vadodara, Gujarat 390007",
              "Baroda Sports Arena, Sevasi TP 3 Rd, Chandramauleshwar Nagar, Gotri, Vadodara, Gujarat 391101",
              "Plot 334, Navrachna University Road, behind 33LE, opposite Nilamber Grandeur, Bhayli, Vadodara, Gujarat 391410",
              "3rd Shot By Strokess, opp. eclipse sports 2, New Alkapuri, Ankodiya, Vadodara, Gujarat 391330",
              "Alkapuri Society, Alkapuri, Vadodara, Gujarat 390007",
              "Inside Adventuraa, Besides Asopalav One West, Sevasi Ring Road, Bhayli, Gujarat 391101",
              "1250, Kendranagar, Vadodara, Gujarat 390025",
              "S No - 170, Jalsa, 72-2, Sevasi - Canal Rd, Vadodara, Gujarat 391110",
              "Pickle Madness, Plot 31/9 B, Sevasi - Canal Rd, next to Pushpak Tennis academy, near Tarak Bunglows, Sevasi, Vadodara, Gujarat 391101",
              "189, Aaryan Party Plot, next to Aatmajyoti Ashram Road, Citizen Society, Ellora Park, Hari Nagar, Vadodara, Gujarat 390023",
              "Elevate Sports, Sevasi - Sindhrot Rd, near Sai Sudha Lawns, New Alkapuri, Khanpur, Vadodara, Gujarat 391330",
              "Ankodiya Rd, behind Doggers Park, opposite Veda Lawns, New Alkapuri, Ankodiya, Vadodara, Gujarat 391330",
              "FF No 99, Jalsa App, TP 1, Priya Talkies Road, near Adventuraa Park, Sevasi, Vadodara, Gujarat 391101",
              "75FF+X8, Manjalpur, Vadodara, Gujarat 390012",
              "Sevasi TP 3 Rd, Chandramauleshwar Nagar, Gotri, Vadodara, Gujarat 391101",
              "Alkapuri Gymkhana, near Baroda High School, Alkapuri, Vadodara, Gujarat 390007",
              "box cricket, Let's Play pickleball arena, Waghodia Rd, in front of amoder, opp. Prime Plaza, Vadodara, Pavlepur, Gujarat 390019"
              ]
court_coordinate = {}
for court_address in court_list:

    lat, long = get_coordinates(court_address, API_KEY)
    court_coordinate[court_address] = (lat, long)

with open('app/vadodara_courts.json', 'w') as f:
    json.dump(court_coordinate, f, indent=4)
