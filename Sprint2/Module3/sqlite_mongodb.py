"""Pipeline example from sqlite to mongodb"""

import sqlite3
import pymongo

PASSWORD = "BVIsO0ZO1GRSDnnr"
DBNAME = "myFirstDatabase"

def connect_to_mongo(password,dbname):
    #Client that connects to MongoDB cluster
    client = pymongo.MongoClient(
        "mongodb+srv://rhiag-UbuntuOS:{}@cluster0.1bqaf.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
        )
    return client

def connect_to_sldb(dbname="../data/rpg_db.sqlite3"):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    return conn, curs

def handle_characters(curs,collection):
    """Handles character pipeline"""
    character_list = curs.execute("SELECT * FROM charactercreator_character")
    
    for character in character_list:
        character_doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8]  
            }
        collection.insert_one(character_doc)

            # # A codier way to do it
    # schema = curs.execute(
    #     "PRAGMA table_info(charactercreator_character)").fetchall()[1:]
    # for character in characters_list:
    #     character_doc = {}
    #     for index, item_tuple in enumerate(schema):
    #         character_doc[item_tuple[1]] = character[index + 1]

    #     collection.insert_one(character_doc)   

def handle_armory(curs,collection):    
    armory_list = curs.execute("SELECT * FROM armory_item")
    for item in armory_list:          
        item_doc = {
            "name": item[1],
            "value": item[2],
            "weight": item[3]
           
        }
    collection.insert_one(item_doc)

def handle_weapons(curs,collection):
    weapon_list = curs.execute("SELECT * FROM armory_weapon")
    for item in weapon_list:
        weapon_doc = {
            "power": item[1]
        }
        collection.insert_one(weapon_doc)

def handle_inventory(curs,collection):
    inventory_list = curs.execute("SELECT * FROM charactercreator_character_inventory")
    for item in inventory_list:
        inventory_doc={
            "character_id": item[0],
            "item_id":item[1]
        }
        collection.insert_one(inventory_doc)
   

if __name__ == "__main__":
    # Creates mongo client 
    mongo_client = connect_to_mongo(PASSWORD,DBNAME)
    # Creates connection to sqlite3
    sl_conn,sl_curs = connect_to_sldb()
    # Reads collection from client.dbname.collection-name
    collection = mongo_client.myFirstDatabase.myFirstDatabase
    collection.delete_many({})

    handle_characters(sl_curs,collection)
    handle_armory(sl_curs,collection)
    handle_weapons(sl_curs,collection)
    handle_inventory(sl_curs,collection)

    print(list(collection.find()))
    sl_curs.close()  
