from google.colab import files
file = files.upload()

import sqlite3
conn = sqlite3.connect('database.sqlite')
print("Database connected successfully")
import pandas as pd
tables = pd.read_sql("""SELECT name FROM sqlite_master WHERE type='table';""", conn)
tables

teams = pd.read_sql("""SELECT * FROM Team;""", conn)

matches = pd.read_sql("""SELECT * FROM Match;""", conn)
matches

MI_wins=pd.read_sql("""SELECT COUNT(*) AS MI_wins FROM Match_Winner== 7;""", conn)

MI_wins

MI_S8_S9 = pd.read_sql("""SELECT COUNT(*) AS MI_S8_S9 FROM Match_Winner== 7 AND Season IN (2018, 2019);""", conn)

MI_S8_S9

new_teams = pd.read_sql("""SELECT * FROM Team WHERE Team_name like 'D%';""", conn)

new_teams

main_max_margins = pd.read_sql("""SELECT MAX(win_Margin) AS Max_Margin FROM Match;""", conn)

main_max_margins