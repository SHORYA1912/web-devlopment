import numpy as np
import pandas as pd
import sqlite3

conn = sqlite3.connect('database.sqlite')
database = 'database.sqlite'

table = pd.read_sql("""SELECT * from sqlite_master where type = 'table'""", conn)

print("============= TABLE IN DATABASE ===============")
print (table)

joined_city = pd.read_sql("""
SELECT  c.country_id,
        c.country_name,
        ci.city_name
        from country c 
        INNER JOIN city ci
        on c.country_id-ci.country_id""", conn)

print ("======= INNER JOIN OUTPUT =======")
print( joined_city)

joined_left = pd.read_sql("""
SELECT * from player LEFT JOIN season on player.Player_id = season.Man_of_the_Series""", conn)

print("======= LEFT_JOINED_output =======")

print(joined_left)

joined_cross = pd.read_sql("""
SELECT  c.Country_id,
        c.Country_name,
        ci.City_name
        from country c
        CROSS JOIN city ci""",conn)

print("======= CROSS_JOINED =======")

union_result = pd.read_sql("""
    SELECT player_name 
    from player
    UNION
    select team_name
    from team""", conn)

print(union_result)

conn.close()