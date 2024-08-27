import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()

name = input("削除したい学生の名前を入力してください：")
age = int(input(f"{name}さんの年齢を入力してください："))

c.execute("DELETE FROM students WHERE name = ? AND age = ?", (name, age))

conn.commit()
conn.close()
