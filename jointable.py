import json
import os 
import sqlite3
import requests

#JOIN table with sad songs 
# start sql table

path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+"songlist.db")
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS sadtimes')
cur.execute("CREATE TABLE sadtimes (id	INTEGER, title TEXT, artist TEXT, sad TEXT, sad_score INTEGER, duration INTEGER)"

cur.execute("INSERT INTO sadtimes SELECT sadsongs.*, Songlist.duration, Songlist.title FROM sadsongs INNER JOIN Songlist ON sadsongs.title=Songlist.title")
cur.execute()

#avg duration of sad songs in sadtimes 
SELECT avg(duration)
FROM sadtimes;

#avg sad_score in sadsongs 
SELECT avg(sad_score)
FROM sadtimes;

#avg duration in songlist 
SELECT avg(duration)
FROM songlist;
