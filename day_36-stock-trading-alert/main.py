# When this program is created, I didn't have access to SMS services so this one is email based
# But later I'm going to make a SMS version of this in features branch

import requests
import config
import datetime
from datetime import timezone
import smtplib as smtp

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={config.stock_key}")
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
print(stock_data)

yesterday = datetime.datetime.now(timezone.utc) - datetime.timedelta(days=1)
day_before = datetime.datetime.now(timezone.utc) - datetime.timedelta(days=2)

yesterday = str(yesterday.date()).split(" ")[0]
day_before = str(day_before.date()).split(" ")[0]

yesterday_data = float(stock_data[yesterday]["4. close"])
day_before_data = float(stock_data[day_before]["4. close"])

percent_change = round(((yesterday_data - day_before_data) / yesterday_data) * 100, 4)


def send_email(percentage: float, title: str, content: str, author: str):
    if percentage < 0:
        msg = f"🔻{round(abs(percentage))}".encode("utf-8")
    else:
        msg = f"🔺{round(percentage)}".encode("utf-8")

    with smtp.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=config.my_email, password=config.password)
        conn.sendmail(from_addr=config.my_email, to_addrs=config.send_email, msg=
                      f"Subject:{COMPANY_NAME}:- {msg}"
                      "\n\n"
                      f"{title}\n{content}"
                      f"\n\n{author}"
                      )


def get_news() -> list:
    news_list = []
    news_response = requests.get(f"https://newsapi.org/v2/everything?q=TSLA&from={day_before}&sortBy=popularity&apiKey={config.news_key}")
    news_response.raise_for_status()
    news_data = news_response.json()
    count = 0

    for i in news_data["articles"]:
        data = {"title": i["title"], "description": i["description"], "author": i["author"]}
        news_list.append(data)
        count += 1
        if count > 2:
            break
    return news_list


if percent_change < -5 or percent_change > 5:
    data = get_news()
    for ii in data:
        send_email(percent_change, ii["title"], ii["description"], ii["author"])
else:
    print("Nah need of news")


# Testing:
test_data = get_news()
for iii in test_data:
    send_email(percent_change, iii["title"], iii["description"], iii["author"])