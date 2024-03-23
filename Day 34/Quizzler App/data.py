import requests
para = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
response = requests.get(url="https://opentdb.com/api.php", params=para)
response.raise_for_status()
question_data = response.json()["results"]
