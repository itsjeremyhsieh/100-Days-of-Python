API_ID = "1917382f"
API_KEY = "d48297c1e0806364b17a871f77d69cd3"
import requests
from datetime import datetime
user = input("Tell me which exercises you did: ")
api_header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
param = {
    "query": user
}

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=ENDPOINT, json=param, headers=api_header)
response.raise_for_status()

result = response.json()["exercises"]
# print(result)

SHEET_ENDPOINT = "https://api.sheety.co/35e9bab59565fe137b7bb08359c28465/myWorkoutsNew/workouts1"
today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

for exercise in result:
    print(exercise["name"])
    header = {
        "Authorization": "Bearer 5tgb6yhn&UJM"
    }
    sheet_param = {
        "workouts1": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url=SHEET_ENDPOINT, json=sheet_param, headers=header)
    response.raise_for_status()
    print(response.text)
