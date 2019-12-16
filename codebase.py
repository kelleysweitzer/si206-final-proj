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

    # # start sql table

    # length = cur.execute("SELECT COUNT (*) FROM Songlist")
    # length = (length.fetchall()[0][0])
    # print(length)

    # verify that the length of the database is 200 so we don't keep making API Calls

        
    # Create Songlist table
    cur.execute("DROP TABLE IF EXISTS Songlist")
    cur.execute("CREATE TABLE Songlist (id TEXT PRIMARY KEY, title TEXT, artist TEXT, duration INTEGER, popularity INTEGER)")
    total = sp.current_user_saved_tracks(limit=1)['total']

    #  Create albumlist table
    cur.execute("DROP TABLE IF EXISTS albumlist")
    cur.execute("CREATE TABLE albumlist (id TEXT PRIMARY KEY, title TEXT, artist TEXT, album TEXT, release_date TEXT)")
    
    # Ensure that we get 200 items
    while last_index < total and last_index < 300:  

        try:
            # makes API call for 20 items
            results = sp.current_user_saved_tracks(limit=20, offset=last_index)

            
            for item in results['items']:
                    _id = item['track']['id']
                    _title = str(item['track']['name'])
                    _artist = item['track']['artists'][0]['name']
                    _duration = item['track']['duration_ms']
                    _popularity = item['track']['popularity']

                    _album = item['track']['album']['name']
                    _release_date = item['track']['album']['release_date']


                    cur.execute("INSERT INTO albumlist (id,title,artist,album,release_date) VALUES (?,?,?,?,?)",(_id, _title,_artist,_album,_release_date))
                    conn.commit()

                    

                    # Populate Songlist DB with name, artist, duration
                    cur.execute("INSERT INTO Songlist (id,title,artist,duration,popularity) VALUES (?,?,?,?,?)",(_id, _title,_artist,_duration,_popularity))
                    conn.commit()

                    last_index += 1

        except:
            pass

else:
    print ("Can't get token for", username)

    