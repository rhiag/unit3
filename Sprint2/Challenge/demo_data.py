"""Part 1: Making and populating a demo database"""

import sqlite3

# Step1: Connecting to the database
conn = sqlite3.connect("./demo_data.sqlite3")
curs = conn.cursor()

# Step2: Create the Database
curs.execute("""CREATE TABLE IF NOT EXISTS demo (s VARCHAR(1) NOT NULL,
                                                 x INTEGER NOT NULL,
                                                 y INTEGER NOT NULL);
            """)

curs.execute("""INSERT INTO demo (s,x,y)
                VALUES ('g',3,9),('v',5,7),('f',8,7);
                """)

conn.commit()

# Step3: Execute SQL queries on demo
curs.execute("SELECT COUNT(*) FROM demo;")
row_count = curs.fetchall()

curs.execute("""SELECT COUNT(*) FROM demo
                WHERE x>= 5 AND y >=5;""")
xy_at_least_5 = curs.fetchall()

curs.execute("""SELECT COUNT(DISTINCT(y)) from demo;""")
unique_y = curs.fetchall()

curs.execute("SELECT * FROM demo;")
rows = curs.fetchall()

curs.close()

# Step4 : Printing Results
print("Row Count: ", row_count)
print("Count of rows where x and y are atleast 5: ", xy_at_least_5)
print("Count of rows of unique y: ", unique_y)
print(rows)
