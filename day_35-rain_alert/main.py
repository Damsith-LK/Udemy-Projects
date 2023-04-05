# Getting some weather data from openweathermap.org

import requests
from key import key

MY_LAT = 7.085899
MY_LONG = 80.033464

params = {"lat": MY_LAT, "lon": MY_LONG, "appid": key}

# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q=Yakkala&appid={key}")
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=params)
response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q=Yakkala&appid={key}')
data = response.json()

print(data)
if response.status_code == 200:
    data = response.json()
    for forecast in data['list']:
        date_time = forecast['dt_txt']
        rainfall = forecast['rain']['3h'] if 'rain' in forecast else 0
        print(f'{date_time}: {rainfall}mm')
else:
    print('Error occurred while getting data from API')