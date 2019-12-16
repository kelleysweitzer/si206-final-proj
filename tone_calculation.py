import matplotlib
import matplotlib.pyplot as plt 
import sqlite3
import json
import unittest

#connecting to database 
conn = sqlite3.connect("songlist.db")
cur = conn.cursor()


#initializes the variables
tone_dict = {}
tentative = 0
analytical = 0
sadness = 0
joy = 0 
anger = 0 
confident = 0
confident_time = 0
fear = 0 

#getting total number of tentative songs and average primary_score
tentative_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Tentative"')
tentative_sum = 0
for row in tentative_songs: 
    tentative += 1
    tentative_sum = row[3]
tentative_average = tentative_sum/tentative
lst = [tentative, tentative_average]
tone_dict["Tentative"] = lst 

#getting total number of analytical songs and average primary_score
analytical_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Analytical"')
analytical_sum = 0 
for row in analytical_songs: 
    analytical += 1
    analytical_sum = row[3]
analytical_average = analytical_sum/analytical
lst = [analytical, analytical_average]
tone_dict["Analytical"] = lst 

#getting total number of sadness songs and average primary_score
sadness_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Sadness"')
sadness_sum =0 
for row in sadness_songs: 
    sadness += 1
    sadness_sum = row[3]
sadness_average = sadness_sum/sadness
lst = [sadness, sadness_average]
tone_dict["Sadness"] = lst 

#getting total number of joy songs and average primary_score
joy_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Joy"')
joy_sum = 0
for row in joy_songs: 
    joy += 1
    joy_sum = row[3]
joy_average = joy_sum/joy
lst = [joy, joy_average]
tone_dict["Joy"] = lst 

#getting total number of angry songs and average primary_score
anger_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Anger"')
anger_sum = 0 
for row in anger_songs: 
    anger += 1
    anger_sum = row[3]
anger_average = anger_sum/anger
lst = [anger, anger_average]
tone_dict["Anger"] = lst 

#getting total number of confident songs and average primary_score
confident_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Confident"')
confident_sum = 0
for row in confident_songs: 
    confident += 1
    confident_sum += row[3]
confident_average = confident_sum/confident
lst = [confident, confident_average]
tone_dict["Confident"] = lst

#getting total number of fear songs and average primary_score
fear_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Fear"')
fear_sum = 0 
for row in fear_songs: 
    fear += 1
    fear_sum += row[3]
fear_average = fear_sum/fear 
lst = [fear, fear_average]
tone_dict["Fear"] = lst 

#turning dictionary into a json file 
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




