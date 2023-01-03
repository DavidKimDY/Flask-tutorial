import sqlite3

conn = sqlite3.connect("database.db")
print("DB connected")

conn.execute("create table users (name text, password text)")
print("users table was created")

conn.close()
