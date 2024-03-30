from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc = response.text

soup = BeautifulSoup(yc, "html.parser")
max = 0
index = 0
cnt = 0
for a in soup.select(selector="td .subline .score"):
    if max < int(a.get_text().split()[0]):
        max = int(a.get_text().split()[0])
        index = cnt
    cnt += 1
print(max)
print(index)


