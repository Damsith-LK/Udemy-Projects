# SMTP = Simple Mail Transfer Protocol
# The email I'm going to send emails, is a gmail

import smtplib as smtp
from day_32.info import *

conn = smtp.SMTP("smtp.gmail.com")
conn.starttls()  # Makes the connection secure
conn.login(user=my_email, password=password)  # Logging to the account
conn.sendmail(from_addr=my_email, to_addrs=send_email, msg="Hello")
conn.close()