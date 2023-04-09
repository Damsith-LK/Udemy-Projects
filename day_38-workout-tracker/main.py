# Here we are going to make a workout tracker program with nutritionnix API and also using google sheets

import config
import requests
import datetime

GENDER = "male"
END_POINT = "https://trackapi.nutritionix.com"

exercise_params = {
    "query": input("What exercises did you do: "),
    "gender": GENDER,
    "weight_kg": 37.5,
    "height_cm": 163.5,
    "age": 14
}
exercise_headers = {
    "x-app-id": config.NIX_ID,
    "x-app-key": config.NIX_KEY,
}

exercise_response = requests.post(url=f"{END_POINT}/v2/natural/exercise", json=exercise_params,
                                  headers=exercise_headers)
data = exercise_response.json()
print(data)



today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

sheet_header = {"Authorization": config.SHEETY_TOKEN}
for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": "{} mins".format(str(exercise["duration_min"])),
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(config.SHEETY_ENDPOINT, json=sheet_inputs, headers=sheet_header)

    print(sheet_response.text)