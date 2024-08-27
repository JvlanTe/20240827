import sqlite3

# データベースに接続するためのコード、ないときは()の中身が生成される。
conn = sqlite3.connect("example.db")

# print("データベースを作成しました。")

c = conn.cursor()

c.execute(
    """
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER NOT NULL
)
"""
)

print("テーブルを作成しました")
conn.close()
