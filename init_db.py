import sqlite3

connection = sqlite3.connect("database.db")

with open("databases/schema.sql") as f:
    connection.executescript(f.read())

connection.commit()
connection.close()

print("Database created successfully")