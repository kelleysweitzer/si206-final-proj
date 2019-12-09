import requests
import json
import sqlite3
import os 
import time
from musixmatch_lyrics_api import * 


path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+"songlist.db")
cur = conn.cursor()
i = 0
last_index = 0

# sql table for top charts 
cur.execute("DROP TABLE IF EXISTS topsongs")
cur.execute("CREATE TABLE topsongs (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, genre TEXT)")


# start sql table for lyrics
cur.execute("DROP TABLE IF EXISTS lyricslist")
cur.execute("CREATE TABLE lyricslist (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, lyrics TEXT)")
pairs = cur.execute("SELECT title, artist FROM songlist")
pairs = pairs.fetchmany(150)
counter = 1

# for pair in pairs: 
#     try:
#         track_name = pair[0]
#         print(pair)
#         artist_name = pair[1]

#         # Finding the lyrics of a song: base url + api method + different parameters + the input that the user put in + API key 
#         api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key 
#         #call the API 
#         request = requests.get(api_call)
#         data = request.json()
#         #data is equivalent to whatever is down at this level of message and body 
#         data = data["message"]["body"]
#         lyrics = data["lyrics"]["lyrics_body"]
#         # print(lyrics)
#         if lyrics != "" or lyrics != " ":
#             cur.execute("INSERT INTO lyricslist (id, title, artist, lyrics) VALUES (?, ?, ?, ?)", (counter, track_name, artist_name, lyrics))
#             conn.commit()
#         counter = counter + 1
#     except:
#         pass

# get top chart songs to populate second sql db
api_call = base_url + 'chart.tracks.get?chart_name=top&page=1&page_size=20&country=xw&f_has_lyrics=1' + api_key

# track_charts + format_url + api_key 
#         #call the API 
request = requests.get(api_call)
data = request.json()
print(data)

i = 1
for song in data['message']['body']['track_list']:
    title = (song['track']['track_name'])
    artist = song['track']['artist_name']
    try:
        genre = song['track']['primary_genres']['music_genre_list'][-1]['music_genre']['music_genre_name']
    except:
        genre = "Unknown"
    cur.execute("INSERT INTO topsongs (id, title,artist,genre) VALUES (?, ?, ?, ?)", (i, title, artist, genre))
    conn.commit()
    i += 1
    print(title, artist, genre)
