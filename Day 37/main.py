import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "1qaz2wsx#EDC",
    "username": "itsjeremyhsieh",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


username = "itsjeremyhsieh"
token = "1qaz2wsx#EDC"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_params = {
    "id": "readinghabit",
    "name": "Reading Habit Tracker",
    "unit": "minute",
    "type": "int",
    "color": "sora",
}
graph_headers = {
    "X-USER-TOKEN": token
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
# print(response.text)

now = datetime.now()

graph_id = "readinghabit"
pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"
pixel_params = {
    "date": now.strftime("%Y%m%d"),
    # "date": "20240325",
    "quantity": "10",
}
pixel_headers = {
    "X-USER-TOKEN": token,
}
# print(now.strftime("%Y%m%d"))
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=pixel_headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/20240325"
update_params = {
    "quantity": "8",
}
update_headers = {
    "X-USER-TOKEN": token,
}
response = requests.put(url=update_endpoint, json=update_params, headers=update_headers)
print(response.text)
