import requests
ENDPOINT = "https://api.sheety.co/35e9bab59565fe137b7bb08359c28465/flightDeals/prices"
USER_ENDPOINT = "https://api.sheety.co/35e9bab59565fe137b7bb08359c28465/flightDeals/users"

header = {"Authorization": "Bearer 5tgb6yhn&UJM"}
class DataManager:
    def __init__(self):
        self.data = {}
    def getData(self):

        response = requests.get(url=ENDPOINT, headers=header)
        self.data = response.json()["prices"]
        return self.data

    def updateData(self, iata, id):
        # for city in self.data:
        new_data = {
            "price":{
                "iataCode": iata,
            }
        }
        response = requests.put(url=f"{ENDPOINT}/{id}", json=new_data, headers=header)
        print(response.text)

    def addUser(self, first, last, email):
        new_data = {
            "user": {
                "firstName": first,
                "lastName": last,
                "email": email,
            }
        }

        response = requests.post(url=USER_ENDPOINT, json=new_data, headers=header)
        response.raise_for_status()
        # print(response.json())

    def getUser(self):
        response = requests.get(url=USER_ENDPOINT, headers=header)
        return response.json()["users"]
