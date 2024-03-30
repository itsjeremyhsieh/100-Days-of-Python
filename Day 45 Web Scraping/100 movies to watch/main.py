import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
result = response.text

soup = BeautifulSoup(result, "html.parser")
rank = []
for movie in soup.select(selector="h3"):
    rank.append(movie.get_text())
rank.reverse()
# print(rank)
with open("movie_ranking.txt", encoding="utf-8", mode="w") as file:
    for i in range(0, len(rank)):
        file.write(f"{rank[i]}\n")
        # print(rank[i])
