# Import this in main.py

import key
from sinch import Client


class SMSSender:
    """Works with sinch in order to send SMSs"""

    def __init__(self):
        self.sinch_client = Client(
            key_id=key.sinch_key,
            key_secret=key.sinch_secret,
            project_id=key.sinch_project_id
        )

    def send_sms(self, send_number: str, message: str):
        """Sends an SMS with given content to the given number"""
        send_batch_response = self.sinch_client.sms.batches.send(
            body=message,
            to=send_number,
            from_=key.sinch_number,
            delivery_report="none"
        )

        print(send_batch_response)

test = SMSSender()
test.send_sms(key.to_number, "Hello this is a testing msg")