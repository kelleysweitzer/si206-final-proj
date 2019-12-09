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

# start sql table
cur.execute("DROP TABLE IF EXISTS lyricslist")
cur.execute("CREATE TABLE lyricslist (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, lyrics TEXT)")
pairs = cur.execute("SELECT title, artist FROM songlist")
pairs = pairs.fetchmany(300)
counter = 1

for pair in pairs: 
    try:
        track_name = pair[0]
        print(pair)
        artist_name = pair[1]

        # Finding the lyrics of a song: base url + api method + different parameters + the input that the user put in + API key 
        api_call = base_url + lyrics_matcher + format_url + artist_search_parameter + artist_name + track_search_parameter + track_name + api_key 
        #call the API 
        request = requests.get(api_call)
        data = request.json()
        #data is equivalent to whatever is down at this level of message and body 
        data = data["message"]["body"]
        lyrics = data["lyrics"]["lyrics_body"]
        # print(lyrics)
        if lyrics != "" or lyrics != " ":
            cur.execute("INSERT INTO lyricslist (id, title, artist, lyrics) VALUES (?, ?, ?, ?)", (counter, track_name, artist_name, lyrics))
            conn.commit()
        counter = counter + 1
    except:
        pass