import requests
import spotipy
import spotipy.util as util
import sqlite3
import json
import os

#   S P O T I F Y     A P I
scope = 'user-library-read'

username = input("Please enter your username: ")

while(len(username) < 1):
    username = input("Invalid Username, try again: ")


# initialize user credentials
token = util.prompt_for_user_token(username,scope,client_id='d194c2865a1547efa27d1f0496272c8a',client_secret='f05c8ca055744cdeb18ee42b9a9441c7',redirect_uri='https://example.com/callback/')


if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = True

    # set up database path
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+"songlist.db")
    cur = conn.cursor()
    i = 0
    last_index = 0

    # start sql table
    cur.execute("DROP TABLE IF EXISTS Songlist")
    cur.execute("CREATE TABLE Songlist (id TEXT PRIMARY KEY, title TEXT, artist TEXT, duration INTEGER, popularity INTEGER)")
    total = sp.current_user_saved_tracks(limit=1)['total']

    while last_index < total or last_index < 100:  

        try:
            # makes API call for 20 items
            results = sp.current_user_saved_tracks(limit=20, offset=last_index)
        except:
            pass


        for item in results['items']:
                _id = item['track']['id']
                _title = str(item['track']['name'])
                _artist = item['track']['artists'][0]['name']
                _duration = item['track']['duration_ms']
                _popularity = item['track']['popularity']
                last_index += 1
                cur.execute("INSERT INTO Songlist (id,title,artist,duration,popularity) VALUES (?,?,?,?,?)",(_id, _title,_artist,_duration,_popularity))
                conn.commit()

else:
    print ("Can't get token for", username)

#Theo test2 