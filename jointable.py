import json
import os 
import sqlite3
#JOIN table with sad songs 
# start sql table
path = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(path+'/'+"songlist.db")
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS sadtimes')
cur.execute('CREATE TABLE sadtimes(id INTEGER PRIMARY KEY, title TEXT, artist TEXT, duration INTEGER, sad_score INTEGER, sad TEXT)')
cur.execute("SELECT * FROM sadsongs INNER JOIN Songlist ON sadsongs.title=Songlist.title")