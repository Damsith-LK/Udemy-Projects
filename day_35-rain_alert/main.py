import requests
import datetime
from key import key

url = f'http://api.openweathermap.org/data/2.5/forecast?q=Yakkala&appid={key}&units=metric'

response = requests.get(url)
response.raise_for_status()

data = response.json()
forecasts = data['list']
current_time = datetime.datetime.now()

id_list = []

for forecast in forecasts:
    date_time = datetime.datetime.fromtimestamp(forecast['dt'])
    if current_time <= date_time <= current_time + datetime.timedelta(hours=12):
        weather_id = forecast['weather'][0]['id']
        w_data = f'{date_time}: {weather_id}'
        id_list.append(w_data)

print(id_list)
for i in id_list:
    if int(i.split(" ")[2]) < 700:
        print("Bring an umbrella")
        break
