import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)
print("Database connected successfully")
import pandas as pd
tables = pd.read_sql("""SELECT name FROM sqlite_master WHERE type='table';""", conn)
tables

matches = pd.read_sql("""SELECT * FROM Match;""", conn)

matches.info()