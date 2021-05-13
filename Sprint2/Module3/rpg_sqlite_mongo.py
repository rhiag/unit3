import sqlite3
import pymongo
import ast

PASSWORD = "BVIsO0ZO1GRSDnnr"
DBNAME = "myFirstDatabase"

def connect_to_mongo(password, dbname):
      
    client = pymongo.MongoClient(
    "mongodb+srv://rhiag-UbuntuOS:{}@cluster0.1bqaf.mongodb.net/{}?retryWrites=true&w=majority"
    .format(password, dbname)
)
    return client
def connect_to_sldb(dbname="../data/rpg_db.sqlite3"):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    return conn, curs
def handle_characters(curs, collection):
    """Handles character pipeline"""
    characters_list = curs.execute(
         """SELECT
                *
            FROM
                charactercreator_character;
        """
        )
    character_docs = []
    for character in characters_list:
        item_list = curs.execute("""
             SELECT item AS item FROM 
             (SELECT
             cc.name, level, exp, hp, strength, intelligence, dexterity, wisdom, ai.name AS item, cc.character_id
             FROM
                 charactercreator_character AS cc
             INNER JOIN
                 charactercreator_character_inventory AS ci ON cc.character_id = ci.character_id
             INNER JOIN
                 armory_item AS ai ON ci.item_id = ai.item_id)
             WHERE character_id = {};""".format(character[0])
        )
        character_doc = {
            "name": character[1],
            "level": character[2],
            "exp": character[3],
            "hp": character[4],
            "strength": character[5],
            "intelligence": character[6],
            "dexterity": character[7],
            "wisdom": character[8],
            "item": list(item_list),
             "weapon": character[9]  
        }
        character_docs.append(character_doc)    
    collection.insert_many(character_docs)
   
if __name__ == "__main__":
    mongo_client = connect_to_mongo(PASSWORD, DBNAME)
    sl_conn, sl_curs = connect_to_sldb()
    collection = mongo_client.myFirstDatabase.myFirstDatabase
    collection.delete_many({})
    handle_characters(sl_curs, collection)
    print(list(collection.find()))
    sl_curs.close()





