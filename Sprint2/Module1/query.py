SELECT_CHARACTERS = "SELECT * FROM charactercreator_character;"

TOTAL_CHARACTERS = "SELECT DISTINCT(name) FROM charactercreator_character;"

TOTAL_SUBCLASS = "SELECT * FROM charactercreator_necromancer;"

TOTAL_ITEMS = "SELECT COUNT(*) FROM armory_item;"

WEAPONS = "SELECT COUNT(*) FROM  armory_item AS ai\
           JOIN armory_weapon AS aw\
           ON ai.item_id = aw.item_ptr_id;"

NON_WEAPONS = "SELECT COUNT (item_id)\
               FROM armory_item\
                WHERE item_id\
                NOT IN (SELECT item_ptr_id \
                        FROM armory_weapon);"

CHARACTER_ITEMS ="SELECT name , COUNT(item_id) AS count\
                FROM charactercreator_character as ccc\
                JOIN charactercreator_character_inventory as ccci\
                ON ccc.character_id == ccci.character_id\
                GROUP BY ccc.character_id\
                LIMIT 20;"

CHARACTER_WEAPONS ="SELECT name, COUNT(*) AS weapons\
                    FROM charactercreator_character AS creator\
                    JOIN charactercreator_character_inventory AS inventory\
                    ON creator.character_id = inventory.character_id\
                    JOIN armory_weapon AS aw\
                    ON aw.item_ptr_id = inventory.item_id\
                    GROUP BY name\
                    LIMIT 20;"

AVG_CHARACTER_ITEMS = "SELECT AVG(COUNT)\
                            FROM (SELECT COUNT(cci.item_id) AS COUNT\
                            FROM charactercreator_character cc,\
                                charactercreator_character_inventory cci\
                            WHERE cc.character_id = cci.character_id\
                            GROUP BY cci.item_id);"

AVG_CHARACTER_WEAPONS="SELECT AVG(weapons)\
                           FROM (SELECT name, COUNT(*) AS weapons\
                                FROM charactercreator_character AS creator\
                                JOIN charactercreator_character_inventory AS inventory\
                                ON creator.character_id = inventory.character_id\
                                JOIN armory_weapon AS aw\
                                ON aw.item_ptr_id = inventory.item_id\
                                GROUP BY name);"

