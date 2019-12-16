import matplotlib
import matplotlib.pyplot as plt 
import sqlite3
import json
import unittest

conn = sqlite3.connect("songlist.db")
cur = conn.cursor()


    #initializes the variables
tone_dict = {}
tentative = 0
analytical = 0
sadness = 0

tentative_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Tentative"')
for row in tentative_songs: 
    if row[2] == "Tentative":
        tentative += 1
tone_dict["Tentative"] = tentative

analytical_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Analytical"')
for row in analytical_songs: 
    if row[2] == "Analytical":
        analytical += 1
tone_dict["Analytical"] = analytical

sadness_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Sadness"')
for row in sadness_songs: 
    if row[2] == "Sadness":
        sadness += 1
tone_dict["Sadness"] = sadness

try:
    filename = open('tonelist.json', 'r')
    file_results = json.loads(filename)
    filename.close()
    filename = open('tonelist.json', 'w')
    for x in tone_dict.keys():
        if x not in file_result.keys():
            filename.write(json.dumps(tone_dict[x]))

except:
    filename = open('tonelist.json', 'w')
    filename.write(json.dumps(tone_dict))




