import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()


name = "rikuto"
age = 18

new_age = int(input(f"{name}さんの新しい年齢を入力してください："))


c.execute("UPDATE students SET age = ? WHERE name = ? AND age = ?", (new_age, name, age))

conn.commit()

conn.close()
