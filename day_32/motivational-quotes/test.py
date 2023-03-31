# This is just for testing

import smtplib as smtp
import datetime as dt
from day_32.info import *
from random import choice

now = dt.datetime.now()
day = now.weekday()
print(day)

if day == 4:  # if today is friday
    with smtp.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=my_email, password=password)
        quotes = []
        with open("quotes.txt", "r") as file:
            for i in file:
                quotes.append(i)
        conn.sendmail(from_addr=my_email, to_addrs=send_email,
                      msg="Subject:Get Motivated!"
                          f"\n\n{choice(quotes)}"
                      )