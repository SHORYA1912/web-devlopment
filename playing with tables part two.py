

import sqlite3

database= 'database.sqlite'
conn = sqlite3.connect(database)
print ("database opened successfully")

import pandas as pd

tables = pd.read_sql("""SELECT name FROM sqlite_master WHERE type='table';""", conn)
tables

Matches = pd.read_sql("""SELECT * FROM Match;""", conn)

Matches.head()

"""CONCLUSION:
-- 12 NUMERIC FEATURES(INTEGER AND NUMERIC) 1 TEXT FEATURE
-- 3 COLUMNS WITH NULL VALUES"""

result1 = pd.read_sql("""SELECT AVG(Win_Margin), Match_winner from Match where Season_Id == 9 GROUP BY Match_Winner ORDER BY AVG(Win_Margin); """, conn)

result1

result2 = pd.read_sql("""SELECT count(distinct venue_id) from Match where Season_Id == 9 """, conn)

result2

result3 = pd.read_sql("""SELECT MIN(Win_Margin), Max(Win_Margin), Avg(Win_Margin), COUNT(DISTINCT(Man_of_the_Match))

FROM Match;""", conn)

result3

result4 = pd.read_sql("""SELECT SUM(Win_Margin) from Match;  """, conn)

result4

print(tables)

print(Matches.head())

print(result1)

print(result2)

print(result3)

print(result4)

