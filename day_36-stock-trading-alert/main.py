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
