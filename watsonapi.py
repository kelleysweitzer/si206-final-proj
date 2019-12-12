import json
import os 
import sqlite3
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator("SzASqEF1bD4L5tzk1wl7YM3Ngk4rkk9wKBT1hJ1w98Wl")
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://gateway.watsonplatform.net/tone-analyzer/api')

# start sql table
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+"songlist.db")
cur = conn.cursor()

# intialize song tones list
cur.execute("DROP TABLE IF EXISTS tonelist")
cur.execute("CREATE TABLE tonelist (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, primary_tone TEXT, primary_score INTEGER)")

# initialize sad songs list
cur.execute("DROP TABLE IF EXISTS sadsongs")
cur.execute("CREATE TABLE sadsongs (id INTEGER PRIMARY KEY, title TEXT, artist TEXT, sad TEXT, sad_score INTEGER)")

# get data from existing lyrics table
data = cur.execute("SELECT title,artist,lyrics FROM lyricslist")
tuples = data.fetchall()
counter = 1

# Loop through 
for song in tuples:

    _title = song[0]
    _artist = song[1]
    lyrics = song[2]
        
    # print(lyrics)

    if lyrics != "" and lyrics != " ":
        try:

            # API Call for the lyrics of that song
            tone_analysis = tone_analyzer.tone(
                    {'text': lyrics},
                    content_type='text/plain',
                    sentences = False
                ).get_result()

            # gets strongest tone in the song
            primary_tone = tone_analysis['document_tone']['tones'][0]['tone_name']
            score = tone_analysis['document_tone']['tones'][0]['score']

            # print(primary_tone)

            # populate tonelist SQL Database
            cur.execute("INSERT INTO tonelist (id, title, artist, primary_tone, primary_score) VALUES (?, ?, ?, ?, ?)", (counter, _title, _artist, primary_tone, score))
            conn.commit()

            # # if it's a sad song, put it in sadsongs table
            if primary_tone == "Sadness":
                cur.execute("INSERT INTO sadsongs (id, title, artist, sad, sad_score) VALUES (?, ?, ?, ?, ?)", (counter, _title, _artist, primary_tone, score))
                conn.commit()


            counter += 1
        
        except:
            print("Error")
            pass
