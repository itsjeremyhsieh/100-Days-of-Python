APIKEY = "JU9SdwL_dxhNpdZOSr3HUk86Id2zamdh"
header = {"apikey": APIKEY}
ENDPOINT_LOCATION = "https://api.tequila.kiwi.com/locations/query"
ENDPOINT_SEARCH = "https://api.tequila.kiwi.com/v2/search"

from data_manager import DataManager
from datetime import datetime, timedelta
import requests
today = datetime.now().strftime("%d/%m/%Y")
tomorrow = datetime.now() + timedelta(days=1)
till = datetime.now() + timedelta(days=(6 * 30))
class FlightSearch():
    def iata(self, city):
        # print("run")
        param = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
            "limit": 10,
            "active_only": True,

        }
        response = requests.get(url=ENDPOINT_LOCATION, headers=header, params=param)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code

    def search(self, city, stop):
        param = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": till.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": stop,
            "curr": "GBP",
        }
        response = requests.get(url=ENDPOINT_SEARCH, headers=header, params=param)
        result = response.json()["data"]

        start_time = result[0]["local_departure"].split("T")[0]
        end_time = result[0]["local_arrival"].split("T")[0]
        # print(f"{city}: {result[0]["price"]}")
        if stop == 4:
            return result[0]["price"], result[0]["flyFrom"], result[0]["flyTo"], result[0][
                "cityTo"], start_time, end_time, result[0]["route"][0]["cityTo"], result[0]["route"][0]["cityCodeTo"]
        else:
            return result[0]["price"], result[0]["flyFrom"], result[0]["flyTo"], result[0]["cityTo"], start_time, end_time
