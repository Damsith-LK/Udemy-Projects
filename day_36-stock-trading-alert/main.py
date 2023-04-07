import requests
import config
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={config.key}")
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
print(data)

yesterday = str(datetime.datetime.today() - datetime.timedelta(days=1)).split(" ")[0]
day_before = str(datetime.datetime.today() - datetime.timedelta(days=2)).split(" ")[0]

yesterday_data = float(data[yesterday]["4. close"])
day_before_data = float(data[day_before]["4. close"])

percent_change = round(((yesterday_data - day_before_data) / yesterday_data) * 100, 4)

if percent_change < -5 or percent_change > 5:
    print("Get News")
else:
    print("Nah need of news")