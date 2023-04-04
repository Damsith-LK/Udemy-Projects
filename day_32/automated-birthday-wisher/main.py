##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv - Done

# 2. Check if today matches a birthday in the birthdays.csv - Done

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv - Done

# 4. Send the letter generated in step 3 to that person's email address. - Done


import smtplib as smtp
from random import choice
import pandas as pd
import datetime as dt
import day_32.info as info

birthday_data = pd.read_csv("birthdays.csv")
bd_list = birthday_data.to_dict(orient="records")

now = dt.datetime.now()
year = now.year
month = now.month
date = now.day

letters = []
for i in range(1, 4):
    with open(f"letter_templates/letter_{i}.txt", "r") as file:
        letters.append(file.read())

for i in bd_list:
    if month == i["month"] and date == i["day"]:
        person = i["name"]
        email = i["email"]
        letter = choice(letters).replace("[NAME]", person)

        with smtp.SMTP('smtp.gmail.com') as conn:
            conn.starttls()
            conn.login(user=info.my_email, password=info.password)
            conn.sendmail(from_addr=info.my_email, to_addrs=email,
                          msg="Subject:Happy Birthday!"
                              f"\n\n{letter}"
                          )
