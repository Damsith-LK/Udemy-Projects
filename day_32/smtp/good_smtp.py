import smtplib as smtp
from day_32.info import *

with smtp.SMTP("smtp.gmail.com") as conn:
    conn.starttls()
    conn.login(user=my_email, password=password)
    conn.sendmail(from_addr=my_email, to_addrs=send_email,
                  msg="Subject:Now here is a subject"
                      "\n\nThis is the content of this Dummy email"
                  )  # We separate the subject from the content by adding "\n\n"