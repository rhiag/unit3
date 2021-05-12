"""PostgreSQL Queries"""

# For postgresql_example.py
SQL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS test_table(
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    age INT
);
"""

SQL_INSERT_DATA="""
INSERT INTO test_table (
    name,
    age
) values 
    ('George',6),
    ('Rick',35);
"""

SQL_SHOW_TABLE = """
SELECT * FROM test_table;
"""

#For ETL pipeline
EXTRACT_CHARACTERS = """
SELECT * FROM charactercreator_character;
"""

CREATE_charactercreator_character = """
CREATE TABLE IF NOT EXISTS charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INT NOT NULL,
    exp INT NOT NULL,
    hp INT NOT NULL,
    strength INT NOT NULL,
    intelligence INT NOT NULL,
    dexterity INT NOT NULL,
    wisdom INT NOT NULL
);
"""
INSERT_charactercreator_character = """
INSERT INTO charactercreator_character (
    character_id,
    name,
    level,
    exp,
    hp,
    strength,
    intelligence,
    dexterity,
    wisdom
  ) VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
  );
"""

EXTRACT_MAGE = """
SELECT * FROM charactercreator_mage
"""


CREATE_charactercreator_mage = """
CREATE TABLE IF NOT EXISTS charactercreator_mage (
    character_ptr_id INT NOT NULL,
    has_pet BOOL NOT NULL,
    mana INT NOT NULL,
    PRIMARY KEY(character_ptr_id),
    CONSTRAINT fk_charactercreator_character
        FOREIGN KEY(character_ptr_id)
            REFERENCES charactercreator_character(character_id)
);
"""

INSERT_charactercreator_mage = """
INSERT INTO charactercreator_mage (
    character_ptr_id,
    has_pet,
    mana
    ) values (
        %s,
        %s,
        %s
    );
    """

EXTRACT_armory_item = """
SELECT * FROM armory_item;
"""

CREATE_armory_item = """
CREATE TABLE IF NOT EXISTS armory_item (
    item_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    value INT NOT NULL,
    weight INT NOT NULL
);
"""

INSERT_armory_item = """
INSERT INTO armory_item(
    item_id,
    name,
    value,
    weight
) values (
    %s,
    %s,
    %s,
    %s
);
"""

EXTRACT_weapon = """
SELECT * FROM armory_weapon;
"""

CREATE_armory_weapon="""
CREATE TABLE IF NOT EXISTS armory_weapon(
    item_ptr_id INT NOT NULL,
    power INT NOT NULL,
    PRIMARY KEY(item_ptr_id),
    CONSTRAINT fk_armory_item
        FOREIGN KEY(item_ptr_id)
            REFERENCES armory_item(item_id)
);
"""

INSERT_armory_weapon="""
INSERT INTO armory_weapon(
    item_ptr_id,
    power
) values(
    %s,
    %s
);
"""