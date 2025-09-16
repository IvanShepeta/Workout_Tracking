import requests
from datetime import datetime
import os

APP_ID = os.getenv("NT_APP_ID")
API_KEY = os.getenv("NT_API_KEY")

exercise_text = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_params = {
    "query": exercise_text,
    "weight_kg": "75",
    "height_cm": "191",
    "age": "22",
}

response = requests.post(url= exercise_endpoint, json=user_params, headers=headers)
result = response.json()

today = datetime.now().strftime("%Y/%m/%d")
now = datetime.now().strftime("%X")
sheets_endpoint = os.getenv("SHEETS_ENDPOINT")

bearer_headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_AUTH')}"
}
for item in result["exercises"]:
    sheet_input = {
        "workout":{
            "date": today,
            "time": now,
            "exercise": item["name"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"],
        }
    }
    sheets_response = requests.post(url=sheets_endpoint, json=sheet_input, headers=bearer_headers)


