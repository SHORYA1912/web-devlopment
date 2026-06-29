import pandas as pd
import sqlite3

database = "og.sqlite"
conn = sqlite3.connect(database)
print("PRINT DATABASE SUCCESSFULLY CONNECTED")

# list tables in the database
table = pd.read_sql("""
	SELECT name
	FROM sqlite_master
	WHERE type='table'
	ORDER BY name;
""", conn)

print("TABLES IN DATA BASE")
print("tables.to_string(index=false)")

print(TEAM TABLE)


csk_matches = -pd.read_sql("""
select""")