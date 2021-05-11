"""
AN example of sqlite3 workflow
"""

import sqlite3
from query import SELECT_CHARACTERS, TOTAL_CHARACTERS,TOTAL_SUBCLASS,TOTAL_ITEMS,WEAPONS,CHARACTER_ITEMS,CHARACTER_WEAPONS,AVG_CHARACTER_ITEMS,AVG_CHARACTER_WEAPONS,NON_WEAPONS

# # Step1 :  Connect to Database
# conn = sqlite3.connect("../data/rpg_db.sqlite3")

# # Step 2: Make a curson from our connection
# curs =  conn.cursor()

# # Step 3: Write your query
# query = "SELECT * FROM charactercreator_character;"

# #STEP 4 :  Execute Query
# curs.execute(query)

# #STEP 5: Fetch results
# results = curs.fetchall()

# print(results)

# Write this in a function
def connect_to_db(db_name="./data/rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

def execute_query(conn,query):
    curs = conn.cursor()
    results = curs.execute(query).fetchall()
    curs.close()
    return results

if __name__ == "__main__":
    conn = connect_to_db()

    characters = execute_query(conn, SELECT_CHARACTERS)
    print(characters)
    print("-------------------------------------------------------------")

    total_char = execute_query(conn, TOTAL_CHARACTERS)
    print(total_char)
    print("-------------------------------------------------------------")

    total_subclass = execute_query(conn, TOTAL_SUBCLASS )
    print(total_subclass)
    print("-------------------------------------------------------------")

    total_items = execute_query(conn, TOTAL_ITEMS )
    print(total_items)
    print("-------------------------------------------------------------")

    weapons = execute_query(conn, WEAPONS )
    print(weapons)
    print("-------------------------------------------------------------")

    non_weapons = execute_query(conn, NON_WEAPONS)
    print(non_weapons)
    print("-------------------------------------------------------------")

    items_per_character = execute_query(conn, CHARACTER_ITEMS)
    print(items_per_character)
    print("-------------------------------------------------------------")

    weapons_per_character = execute_query(conn, CHARACTER_WEAPONS)
    print(weapons_per_character)
    print("-------------------------------------------------------------")

    avg_items = execute_query(conn, AVG_CHARACTER_ITEMS)
    print(avg_items)
    print("-------------------------------------------------------------")

    avg_weapons = execute_query(conn, AVG_CHARACTER_WEAPONS)
    print(avg_weapons)