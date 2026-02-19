import requests
import json

url = "https://api.hudle.in/api/v1/venues/7fdd3ff5-8fea-4862-89b9-28ce34e2f7ff/facilities/5e9ee6ad-f5a9-408a-85b5-e4e428bacc96/slots?start_date=2025-08-10&end_date=2025-08-13&grid=1"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "api-secret": "hudle-api1798@prod",
    "authorization": "Bearer YOUR_TOKEN_HERE",
    "origin": "https://hudle.in",
    "referer": "https://hudle.in/",
    "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "x-app-id": "250101575373613800053736900144030"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
else:
    print(f"Request failed: {response.status_code} - {response.text}")
