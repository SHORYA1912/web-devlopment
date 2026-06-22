import sqlite3

conn = sqlite3.connect('database.sqlite')

print("Database connected successfully")

conn.execute("""CREATE TABLE IF NOT EXISTS CLASS_10
            (SNO INT PRIMARY KEY NOT NULL,
            ROLL_NO INT NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT DEFAULT (15),
            GENDER TEXT NOT NULL,
            EMAIL_ID TEXT NOT NULL,
            CONTACT_NO INT NOT NULL);""")

print("Table created successfully")

conn.execute("""INSERT INTO CLASS_10
              (SNO, ROLL_NO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NO) 
             values ("1", "1", "ALLEN", "15", "MALE", "allen@email.com", "1234567"); """)

conn.execute("""INSERT INTO CLASS_10
              (SNO, ROLL_NO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NO) 
             values ('2', '2', 'AISHA', '15', 'FEMALE', 'aisha@email.com', '9080900'); """)

conn.execute("""INSERT INTO CLASS_10
              (SNO, ROLL_NO, NAME, AGE, GENDER, EMAIL_ID, CONTACT_NO) 
             values ('3', '3', 'JEFF', '15', 'MALE', 'jeff@email.com', '9900900'); """)

conn.commit()

print("Records inserted successfully")

import pandas as pd

tables = pd.read_sql("""SELECT * from sqlite_master WHERE type='table';""", conn)

tables
cursor = conn.execute("SELECT * FROM CLASS_10")
class_10b = pd.read_sql("""SELECT * FROM CLASS_10;""", conn)

class_10b.head()