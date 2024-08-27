import sqlite3

conn = sqlite3.connect("example.db")

c = conn.cursor()

name = input("名前を入力してください：")
age = int(input("年齢を入力してください："))

# こういう書き方
c.execute("INSERT INTO students (name , age) VALUES (? , ?)", (name, age))

conn.commit()

conn.close()
