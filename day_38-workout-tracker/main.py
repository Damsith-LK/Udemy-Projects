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


# ----------------------- FUNCTIONS START HERE ------------------------- #
def get_date() -> str:
    day = input("When did you do these exercises? (day before yesterday or yesterday or today): ").lower()
    if day == 'day before yesterday':
        day = datetime.datetime.now() - datetime.timedelta(days=2)
    elif day == "yesterday":
        day = datetime.datetime.now() - datetime.timedelta(days=1)
    else:
        day = datetime.datetime.now()

    return str(day.strftime("%d/%m/%Y"))

def get_time() -> str:
    time = input("At what time of the day did you these glorious exercises (eg - 18:30 or now): ").lower()
    if ":" not in time and time != "now":
        quit("Invalid Input")
    if time == "now":
        time = datetime.datetime.now().strftime("%X")
    else:
        time += ":00"

    return time
# ----------------------------- FUNCTIONS END HERE --------------------------- #


date = get_date()
time = get_time()
print(date, time)

sheet_header = {"Authorization": config.SHEETY_TOKEN}

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": "{} mins".format(str(exercise["duration_min"])),
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(config.SHEETY_ENDPOINT, json=sheet_inputs, headers=sheet_header)

    print(sheet_response.text)