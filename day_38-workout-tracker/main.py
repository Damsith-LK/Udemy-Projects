# Here we are going to make a workout tracker program with nutritionnix API and also using google sheets

import config
import requests

GENDER = "male"
END_POINT = "https://trackapi.nutritionix.com"
exercise_params = {
    "query": "did 100 push-ups in 15 minutes and did 6 sets of 4 pull-ups and cycled 500m",
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
print(exercise_response.text)
