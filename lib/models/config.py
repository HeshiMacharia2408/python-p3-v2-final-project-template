import sqlite3

conn = sqlite3.connect('./db/music.db')
cursor = conn.cursor()