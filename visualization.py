import matplotlib
import matplotlib.pyplot as plt 
import sqlite3
import json

conn = sqlite3.connect("songlist.db")
cur = conn.cursor()

def tone_number(databse):

    #initializes the variables
    tone_dict = {}
    tentative = 0
    analytical = 0
    sadness = 0
    joy = 0 
    anger = 0 
    confident = 0
    fear = 0 

    #getting total number of tentative songs
    tentative_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Tentative"')
    for row in tentative_songs: 
        tentative += 1
    tone_dict["Tentative"] = tentative 

    #getting total number of analytical songs 
    analytical_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Analytical"')
    for row in analytical_songs: 
        analytical += 1
    tone_dict["Analytical"] = analytical 

    #getting total number of sadness songs 
    sadness_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Sadness"')
    for row in sadness_songs: 
        sadness += 1
    tone_dict["Sadness"] = sadness 

    #getting total number of joy songs 
    joy_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Joy"')
    for row in joy_songs: 
        joy += 1
    tone_dict["Joy"] = joy

    #getting total number of angry songs 
    anger_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Anger"')
    for row in anger_songs: 
        anger += 1
    tone_dict["Anger"] = anger  

    #getting total number of confident songs and average primary_score
    confident_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Confident"')
    for row in confident_songs: 
        confident += 1
    tone_dict["Confident"] = confident

    #getting total number of fear songs and average primary_score
    fear_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Fear"')
    for row in fear_songs: 
        fear += 1
    tone_dict["Fear"] = fear

    return tone_dict

def tone_number_visualization(tone_dict):
    #sets lists that will be used for x and y values
    names = tone_dict.keys()
    vals = tone_dict.values()
    
    #creates graph
    fig, ax = plt.subplots()
    
    #gives value for graph and sets color of each bar
    plt.bar(names, vals, color = ['red', 'blue', 'cyan', 'yellow', 'pink', 'green', 'orange'])

    #sets more information for graph axis
    ax.set_xlabel("Tone Name")
    ax.set_ylabel("# of Songs")
    ax.set_title("Songs per Tone")

    #presents the graph
    plt.show()

def tone_score_average(database):
    #initializes the variables
    tone_score_dict = {}
    tentative = 0
    analytical = 0
    sadness = 0
    joy = 0 
    anger = 0 
    confident = 0
    fear = 0 

    #getting total number of tentative songs and average primary_score
    tentative_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Tentative"')
    tentative_sum = 0
    for row in tentative_songs: 
        tentative += 1
        tentative_sum = row[3]
    tentative_average = tentative_sum/tentative
    tone_score_dict["Tentative"] = tentative_average

    #getting total number of analytical songs and average primary_score
    analytical_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Analytical"')
    analytical_sum = 0 
    for row in analytical_songs: 
        analytical += 1
        analytical_sum = row[3]
    analytical_average = analytical_sum/analytical
    tone_score_dict["Analytical"] = analytical_average 

    #getting total number of sadness songs and average primary_score
    sadness_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Sadness"')
    sadness_sum =0 
    for row in sadness_songs: 
        sadness += 1
        sadness_sum = row[3]
    sadness_average = sadness_sum/sadness
    tone_score_dict["Sadness"] = sadness_average 

    #getting total number of joy songs and average primary_score
    joy_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Joy"')
    joy_sum = 0
    for row in joy_songs: 
        joy += 1
        joy_sum = row[3]
    joy_average = joy_sum/joy
    tone_score_dict["Joy"] = joy_average 

    #getting total number of angry songs and average primary_score
    anger_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Anger"')
    anger_sum = 0 
    for row in anger_songs: 
        anger += 1
        anger_sum = row[3]
    anger_average = anger_sum/anger
    tone_score_dict["Anger"] = anger_average

    #getting total number of confident songs and average primary_score
    confident_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Confident"')
    confident_sum = 0
    for row in confident_songs: 
        confident += 1
        confident_sum += row[3]
    confident_average = confident_sum/confident
    tone_score_dict["Confident"] = confident_average

    #getting total number of fear songs and average primary_score
    fear_songs = cur.execute('SELECT title, artist, primary_tone, primary_score FROM tonelist WHERE primary_tone = "Fear"')
    fear_sum = 0 
    for row in fear_songs: 
        fear += 1
        fear_sum += row[3]
    fear_average = fear_sum/fear 
    tone_score_dict["Fear"] = fear_average
    
    return tone_score_dict 

def tone_score_visualization(tone_score_dict):
    #sets lists that will be used for x and y values
    names = tone_score_dict.keys()
    vals = tone_score_dict.values()
    
    #creates graph
    fig, ax = plt.subplots()
    
    #gives value for graph and sets color of each bar
    plt.bar(names, vals, color = ['pink', 'green', 'orange', 'yellow', 'red', 'blue', 'cyan'])

    #sets more information for graph axis
    ax.set_xlabel("Tone Name")
    ax.set_ylabel("Average Primary Score")
    ax.set_title("Average Primary Score for Each Tone")

    #presents the graph
    plt.show()

def popularity_boxplot(database):
    popularity_data = cur.execute('SELECT popularity FROM Songlist')
    scores = []
    data = popularity_data.fetchall()
    for tup in data:
        scores.append(tup[0])
    # print (scores)

        # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)

    # Create the boxplot
    bp = ax.boxplot(scores)

    ax.set_xlabel("Popularity Score")
    ax.set_title("Range of Popularity Scores for all Spotify Songs")

    plt.show()

def duration_boxplot(database):
    popularity_data = cur.execute('SELECT duration FROM Songlist')
    scores = []
    data = popularity_data.fetchall()
    for tup in data:
        seconds = tup[0]/1000
        
        scores.append(seconds)
    # print (scores)

        # Create a figure instance
    fig = plt.figure(1, figsize=(9, 6))

    # Create an axes instance
    ax = fig.add_subplot(111)

    # Create the boxplot
    bp = ax.boxplot(scores)

    ax.set_xlabel("Duration")
    ax.set_title("Range of duration for all Spotify Songs")

    plt.show()
        

#number of songs per tone bar graph 
# tone_dict = tone_number('songlist.db')
# tone_number_visualization(tone_dict)

# #average primary score number per tone bar graph 
# tone_score_dict = tone_score_average('songlist.db')
# tone_score_visualization(tone_score_dict)

# boxplot of popularity
popularity_data = popularity_boxplot('songlist.db')
duration = duration_boxplot('songlist.db')