# import requests

# # List of court data entries
# courts = [
#     {
#         "name": "Vadodara Pickleball Arena",
#         "address": "Plot 19, Old Padra Rd, next to Sera Pizzeria, near Hanuman temple, JP Nagar, Sukrutinagar, Diwalipura, Vadodara, Gujarat 390015",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 3,
#         "opening_time": "06:00:00",
#         "closing_time": "01:00:00"
#     },
#     {
#         "name": "Smash Pickleball Club & Cafe",
#         "address": "Smash, b, Fitness MMA, h Dojo, Vasna - Bhayli Main Rd, nr. Kalyan Party Plot, Krishnadham Society, Saiyed Vasna, Vadodara, Gujarat 390007",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 4,
#         "opening_time": "06:00:00",
#         "closing_time": "00:00:00"
#     },
#     {
#         "name": "The Pickleball Centre",
#         "address": "849F+265, Sevasi, Vadodara, Khanpur, Gujarat 391101",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 2,
#         "opening_time": "06:00:00",
#         "closing_time": "00:00:00"
#     },
#     {
#         "name": "Alpha Arena",
#         "address": "189, Aaryan Party Plot, next to Aatmajyoti Ashram Road, Citizen Society, Ellora Park, Hari Nagar, Vadodara, Gujarat 390023",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 4,
#         "opening_time": "06:00:00",
#         "closing_time": "00:00:00"
#     },
#     {
#         "name": "Pickle Madness",
#         "address": "Pickle Madness, Plot 31/9 B, Sevasi - Canal Rd, next to Pushpak Tennis academy, near Tarak Bunglows, Sevasi, Vadodara, Gujarat 391101",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 3,
#         "opening_time": "06:00:00",
#         "closing_time": "01:00:00"
#     },
#     {
#         "name": "Dropshot Pickleball Academy & Club",
#         "address": "Plot 334, Navrachna University Road, behind 33LE, opposite Nilamber Grandeur, Bhayli, Vadodara, Gujarat 391410",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 4,
#         "opening_time": "06:00:00",
#         "closing_time": "01:00:00"
#     },
#     {
#         "name": "United Pickleball",
#         "address": "S No - 170, Jalsa, 72-2, Sevasi - Canal Rd, Vadodara, Gujarat 391110",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 4,
#         "opening_time": "06:00:00",
#         "closing_time": "00:00:00"
#     },
#     {
#         "name": "Athletes Arena | Pickle Ball, Turf and Paddle/Padel Tennis Club",
#         "address": "FF No 99, Jalsa App, TP 1, Priya Talkies Road, near Adventuraa Park, Sevasi, Vadodara, Gujarat 391101",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 2,
#         "opening_time": "00:00:00",
#         "closing_time": "00:00:00"
#     },
#     {
#         "name": "MatchPoint Vadodara",
#         "address": "Ankodiya Rd, behind Doggers Park, opposite Veda Lawns, New Alkapuri, Ankodiya, Vadodara, Gujarat 391330",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 4,
#         "opening_time": "06:00:00",
#         "closing_time": "01:00:00"
#     },
#     {
#         "name": "adVantaJe Tennis & Fitness",
#         "address": "Alkapuri Gymkhana, near Baroda High School, Alkapuri, Vadodara, Gujarat 390007",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 1,
#         "opening_time": "06:00:00",
#         "closing_time": "21:00:00"
#     },
#     {
#         "name": "Elevate Sports",
#         "address": "Elevate Sports, Sevasi - Sindhrot Rd, near Sai Sudha Lawns, New Alkapuri, Khanpur, Vadodara, Gujarat 391330",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 4,
#         "opening_time": "06:00:00",
#         "closing_time": "02:00:00"
#     },
#     {
#         "name": "MatchPoint Vadodara",
#         "address": "Ankodiya Rd, behind Doggers Park, opposite Veda Lawns, New Alkapuri, Ankodiya, Vadodara, Gujarat 391330",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 4,
#         "opening_time": "06:00:00",
#         "closing_time": "01:00:00"
#     },
#     {
#         "name": "MatchPoint Vadodara",
#         "address": "Ankodiya Rd, behind Doggers Park, opposite Veda Lawns, New Alkapuri, Ankodiya, Vadodara, Gujarat 391330",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 4,
#         "opening_time": "06:00:00",
#         "closing_time": "01:00:00"
#     },
#     {
#         "name": "MatchPoint Vadodara",
#         "address": "Ankodiya Rd, behind Doggers Park, opposite Veda Lawns, New Alkapuri, Ankodiya, Vadodara, Gujarat 391330",
#         "city": "Vadodara",
#         "state": "Gujarat",
#         "contact_number": "0000000000",
#         "number_of_courts": 4,
#         "opening_time": "06:00:00",
#         "closing_time": "01:00:00"
#     }
# ]

# # Send each court to the API
# url = "http://127.0.0.1:8000/api/v1/courts/"
# for court in courts:
#     response = requests.post(url, json=court)
#     print(f"Status: {response.status_code}, Response: {response.json()}")
