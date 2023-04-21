import smtplib as smtp
from email.mime.text import MIMEText
import config


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def __init__(self):
        pass

    def send_email(self, price_in_gbp: int, des_city_name: str, des_city_code: str, outbound_date: str,
                   inbound_date: str, stop_overs: int or None, via_cities: list[str] or None, user_email: str,
                   dep_city_name="Colombo", dep_city_code="CMB"):
        """Gets the relevant data in parameters and send an e-mail with those data. Dates should be entered in the format YYYY-MM-DD"""
        stop_over_msg = ""
        if stop_overs == 0 or stop_overs is None:
            stop_over_msg = "Flight has no stop overs"
        elif stop_overs == 1:
            stop_over_msg = f"Flight has {stop_overs} stop over, via city {via_cities[0]}"
        else:
            stop_over_msg = f"Flight has {stop_overs} stop overs, via cities: {', '.join(via_cities)}"

        subject = "Low Price Alert!"
        body = f"Only £{price_in_gbp} to fly from {dep_city_name}-{dep_city_code} to {des_city_name}-{des_city_code}," \
               f" from {outbound_date} to {inbound_date}" \
               f"\n\n {stop_over_msg}"

        with smtp.SMTP('smtp.gmail.com', 587) as conn:
            conn.ehlo()
            conn.starttls()
            conn.login(user=config.my_email, password=config.password)
            email_body = MIMEText(body, 'plain', 'utf-8')
            email_body['Subject'] = subject
            email_body['From'] = config.my_email
            email_body['To'] = user_email
            conn.send_message(email_body)
