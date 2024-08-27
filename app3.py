import sqlite3

conn = sqlite3.connect("example.db")

c = conn.cursor()

c.execute("SELECT * FROM students")

rows = c.fetchall()

for row in rows:
    print(row)

conn.close
