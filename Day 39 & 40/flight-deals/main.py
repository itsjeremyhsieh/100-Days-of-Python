#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
import requests
from pprint import pprint
NotificationManager = NotificationManager()
FlightSearch = FlightSearch()
DataManager = DataManager()
data = DataManager.getData()
# DataManager.getUser()
# print(data)
member = False
print("Welcome to Jeremy's Flight Club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_2 = input("Type your email again.\n")
if email == email_2:
    DataManager.addUser(first_name, last_name, email)
    print("You're in the club!")
    member = True

if member:
    for city in data:
        if city["iataCode"] == "":
            # DataManager.updateData(city["id"])
            DataManager.updateData(FlightSearch.iata(city["city"]), city["id"])
        try:
            price, flyfrom, flyto, cityto, start_time, end_time = FlightSearch.search(city["iataCode"], 2)
            # print(cityto)
            if city["Lowest Price"]:
                print(f"Direct flight to {city['city']} - {city['iataCode']} found!")
            if city["Lowest Price"] > price:
                message = f"Low price alert! Only £{price} to fly from London-{flyfrom} to {cityto}-{flyto}, from {start_time} to {end_time}."
                NotificationManager.sendemails(DataManager.getUser(), message)
        #     NotificationManager.sendNotification(message)
        except:
            try:

                price, flyfrom, flyto, cityto, start_time, end_time, stopover_city, stopover_code = FlightSearch.search(city["iataCode"], 4)
                message = f"Low price alert! Only £{price} to fly from London-{flyfrom} to {cityto}-{flyto}, from {start_time} to {end_time}."
                if not city['iataCode'] == stopover_code: # weird api error
                    print(f"No direct flight to {city['city']} - {city['iataCode']}")
                    print(f"Flight has 1 stop over, via {stopover_city} - {stopover_code}.")
                    message += f"Flight has 1 stop over, via {stopover_city} - {stopover_code}."
                    NotificationManager.sendemails(DataManager.getUser(), message)
                else:
                    print(f"Direct flight to {city['city']} - {city['iataCode']} found!")
                    NotificationManager.sendemails(DataManager.getUser(), message)
            except:
                print(f"No flight within 1 stop over to {city['city']} - {city['iataCode']} found.")
                continue