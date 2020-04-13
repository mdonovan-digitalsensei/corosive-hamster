import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
#cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

users = [
    (1, 'dave', 'asdf'),
    (2, 'sam', 'test'),
    (3, 'will', '1234'),
]

cursor.executemany(insert_query,users)
connection.commit()
connection.close()
