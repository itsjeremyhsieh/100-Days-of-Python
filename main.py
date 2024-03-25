STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
twilio_sid = "ACcec6267161fc94342d096e4cd7131d5f"
twilio_token = "f7fc13ca7e9f0ee476a312a3c800a379"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_NEWS = "3ef0ac4085654bea9fd6943fc5bfc5a4"
API_STOCK = "FQ848W6JD3OI40IL"
para_news = {
    "apiKey": API_NEWS,
    "q": "tesla",
    "qInTitle": COMPANY_NAME,
}
para_stock = {
    "apikey": API_STOCK,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK
}


import requests
from twilio.rest import Client

response = requests.get(url=STOCK_ENDPOINT, params=para_stock)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yest_closing_price = data_list[0]["4. close"]
day_b4_yest_closing_price = data_list[1]["4. close"]
difference = float(yest_closing_price) - float(day_b4_yest_closing_price)
print(difference)
up_down = ""
if difference > 0:
    up_down = "🔺"
elif difference < 0:
    up_down = "🔻"

diff_percent = round(abs(difference) / float(yest_closing_price) * 100)
if diff_percent >= 1:
    response = requests.get(url=NEWS_ENDPOINT, params=para_news)
    response.raise_for_status()
    news = response.json()["articles"][:3]
    # print(news)
    news_list = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']} \nBrief: {article['description']}" for article in news]
    # print(news_list)
    client = Client(twilio_sid, twilio_token)
    for article in news_list:
        message = client.messages.create(
            body=article,
            from_="+16562192808",
            to="+886987301813"
        )
