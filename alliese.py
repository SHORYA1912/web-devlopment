# Import necessary libraries

import pandas as pd

import sqlite3

# Path to the SQLite database file

database = "database.sqlite"

# Connect to the database

conn = sqlite3.connect(database)

print("Connected to the database successfully!\n")

# Display all tables in the database

tables = pd.read_sql("""

SELECT *

FROM sqlite_master

WHERE type='table';

""", conn)

print("========== TABLES IN DATABASE ==========\n")

print(tables.to_string(index=False))

# Fetch match details using aliases

match_details = pd.read_sql("""

SELECT

m.Season_Id,

m.Match_Id,

v.Venue_Name,

c.City_Name,

t.Team_Name AS Winner

FROM Match AS m

INNER JOIN Venue AS v

ON m.Venue_Id = v.Venue_Id

INNER JOIN City AS c

ON v.City_Id = c.City_Id

INNER JOIN Team AS t

ON m.Match_Winner = t.Team_Id;

""", conn)

print("\n========== MATCH DETAILS ==========\n")

print(match_details.to_string(index=False))

# Close the connection

conn.close()

print("\nDatabase connection closed.")