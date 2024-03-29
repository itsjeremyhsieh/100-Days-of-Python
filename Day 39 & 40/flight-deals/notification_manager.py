twilio_sid = "ACcec6267161fc94342d096e4cd7131d5f"
twilio_token = "80e0976df162693519949805a231edba"
email = "jeremy.life0107@gmail.com"
password = "pgmsaalgjzlfvngh"

import requests
import smtplib
from twilio.rest import Client


class NotificationManager:

    def sendNotification(self, message):
        client = Client(twilio_sid, twilio_token)
        send = client.messages \
            .create(body=message,
                    from_="+16562192808",
                    to="+886987301813")
        print(send.status)

    def sendemails(self, users, msg):
        for user in users:

            first = user['firstName']
            last = user['lastName']
            user_email = user['email']

            with smtplib.SMTP("smtp.gmail.com") as connection:
                print("Sending")
                connection.starttls()  # secure connection
                connection.login(user=email, password=password)
                status = connection.sendmail(from_addr=email, to_addrs=user_email, msg=f"subject:New flight "
                                                                                       f"deal!\n\nDear {first}:\n{msg}")
                print(status)
