import sqlite3
conn = sqlite3.connect('database.sqlite')

conn . execute('''CREATE TABLE IF NOT EXISTS STUDENTS7
             (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
               );''')

conn.execute("INSERT INTO STUDENTS7 (name, age) VALUES ('SARA', 15);")
conn.execute("INSERT INTO STUDENTS7 (name, age) VALUES ('ALI', 14);")

conn.commit()
conn.close()

print ("DATABASE SUCCESSFULLY CREATED")