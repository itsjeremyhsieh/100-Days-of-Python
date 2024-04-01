import requests
import smtplib
from bs4 import BeautifulSoup

email = "jeremy.life0107@gmail.com"
password = "pgmsaalgjzlfvngh"

URL = "https://www.amazon.com/Anniversary-Paperback-Volumes-Limited-Original/dp/1637990049/ref=sr_1_8?crid=1MKSX6Y2RBL51&dib=eyJ2IjoiMSJ9.jeL5AORfIvbSuiYJ1SgoMCXiKRtVdBBg14ycoN6s_wKVjfVYZJwm8A9VlhZPspmfJDMYQN0G3HlYMfY6VKmJixH9fmQQmnbmMbgYVayRhfAw05Tc-Q6L7YRQSio13TZtUhf7FjlQ-h1_3Q6CxDhsvyNzLlOEN6ykYbIswijMKjkpk4XgjJsjT_ATF1FgWQ2znrSIAfBzGNbDDib2ZjwGHVuYrH04Mf11hN1hBG18nR0xvzYWs4RqGvA8jlcaaWezVwLk9VYrGAS3aO_bZi8tnuBl40VJDEifNnDbzZ7MRG0.1twgCWNq-TJgtE5u5DykPtoPws2TfIPdQnISPsMhMH0&dib_tag=se&keywords=harry+potter+books&qid=1711972500&sprefix=harry+potter+bo%2Caps%2C278&sr=8-8"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6",
}

response = requests.get(url=URL, headers=header)
# print(response.text)

soup = BeautifulSoup(response.text, "lxml")
price = soup.find(id="price")
price = float(price.get_text().replace("$", ""))
print(price)

if price < 75:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secure connection
        connection.login(user=email, password=password)
        status = connection.sendmail(from_addr=email, to_addrs=email, msg=f"subject:Amazon Price Alert! "
                                                                               f"\n\n25 Year Anniversary Editon of Harry Potter Paperback Full Book Set Volumes 1-7 (Limited Edition, Original cover) is now ${price}! \n{URL}")
