import smtplib as smtp
from email.mime.text import MIMEText
import config


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self):
        pass

    def send_email(self, price_in_gbp: int, des_city_name: str, des_city_code: str, outbound_date: str,
                   inbound_date: str, dep_city_name="Colombo", dep_city_code="CMB"):
        """Gets the relevant data in parameters and send an e-mail with those data. Dates should be entered in the format YYYY-MM-DD"""
        subject = "Low Price Alert!"
        body = f"Only £{price_in_gbp} to fly from {dep_city_name}-{dep_city_code} to {des_city_name}-{des_city_code}," \
            f" from {outbound_date} to {inbound_date}"

        with smtp.SMTP('smtp.gmail.com', 587) as conn:
            conn.ehlo()
            conn.starttls()
            conn.login(user=config.my_email, password=config.password)
            email_body = MIMEText(body, 'plain', 'utf-8')
            email_body['Subject'] = subject
            email_body['From'] = config.my_email
            email_body['To'] = config.send_email
            conn.send_message(email_body)
