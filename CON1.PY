import sqlite3

conn = sqlite3.connect('database.sqlite')

print("Database connected successfully")

conn.execute("""CREATE TABLE IF NOT EXISTS CLASS_10
            (SNO INT NOT NULL,
            ROLL_NO INT NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT,
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
print(cursor.fetchall())
class_10b = pd.read_sql("""SELECT * FROM CLASS_10;""", conn)

print("Data from CLASS_10:")
print(class_10b)

null_counts = class_10b.isnull().sum()
print("Null value counts per column:")
print(null_counts)

null_rows = class_10b[class_10b.isnull().any(axis=1)]
print("Rows with null values:")
print(null_rows)