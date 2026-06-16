import sqlite3

conn = sqlite3.connect('database.sqlite')
database = 'database.sqlite'
print("Database connected successfully")

import pandas as pd

tables = pd.read_sql("""SELECT name FROM sqlite_master WHERE type='table';""", conn)
tables

matches = pd.read_sql("""SELECT * FROM Match;""", conn)
matches

distinct = pd.read_sql("""SELECT DISTINCT(Match_winner) FROM Match;""", conn)

distinct

group_by = pd.read_sql("""SELECT Match_winner, COUNT(*) FROM Match GROUP BY Match_winner;""", conn)

group_by

order_by = pd.read_sql("""SELECT Match_winner, COUNT(*) FROM Match GROUP BY Match_winner ORDER BY COUNT(*) DESC;""", conn)

order_by

print(tables)
print(matches)
print(distinct)
print(group_by)
print(order_by)
