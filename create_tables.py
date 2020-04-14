import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, item text, price text)"
cursor.execute(create_table)

connection.commit()
connection.close()