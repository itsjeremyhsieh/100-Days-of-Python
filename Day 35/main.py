from password import *

import requests
from twilio.rest import Client

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
weather_data = data['list']
will_rain = False
for forecast in weather_data:
    if int(forecast["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(twilio_sid, twilio_token)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an umbrella!",
                from_="+16562192808",
                to="+886987301813")
    print(message.status)
print("Code executed.")
