import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime
from bs4 import BeautifulSoup
CLIENT_ID = "60fd516fea11471f8cbb0b64e9041e42"
CLIENT_SECRET = "475afcb35f1f4d5b8c871aa77ab8d095"
user_date = input("Which year do you want to travel to? Type the date in YYYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/"+user_date+"/"
try:
    response = requests.get(url=URL)
    result = response.text
    soup = BeautifulSoup(result, "html.parser")
    rank = []
    for song in soup.select(selector="li #title-of-a-story"):
        song_name = song.get_text()
        song_name = song_name.replace('\n', '')
        song_name = song_name.replace('\t', '')
        rank.append(song_name)
    # print(rank)
    year = user_date.split("-")[0]
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            show_dialog=True,
            cache_path="token.txt",
            username="itsjeremyhsieh",
            )
        )
    user_id = sp.current_user()["id"]
    urls = []
    for song in rank:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        print(result)
        try:
            url = result["tracks"]["items"][0]["uri"]
            urls.append(url)
        except IndexError:
            print(f"{song} not found in Spotify. Skipped.")
    playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=urls)
    print("Playlist created.")
except:
    print("URL not found")
    pass

