import smtplib as smtp
import datetime as dt
from random import choice
from day_32.info import *

now = dt.datetime.now()
day = now.weekday()

if day == 0:
    with smtp.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        quotes = []

        with open("quotes.txt", "r") as file:
            for i in file:
                quotes.append(i)
        conn.sendmail(from_addr=my_email, to_addrs=send_email,
                      msg="Subject:Monday Motivation\n\n"
                          f"{choice(quotes)}")

else:
    print(f"Today's not Monday. Today is {day}")
