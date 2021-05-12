"""Setting up a database for Titanic.csv"""

import pandas as pd
import psycopg2 as pg2
from titanic_query import CREATE_TITANIC_TABLE,SHOW_TITANIC


DBNAME = "?"
USER = '?'
PASSWORD = "?"
HOST = "?"

url = "https://raw.githubusercontent.com/LambdaSchool/data-science-practice-datasets/main/unit_1/Titanic/Titanic.csv"

df = pd.read_csv(url)
print(df.shape)

df.rename(columns= {'Siblings/Spouses_Aboard':'Sibling_Spouse_Aboard',
'Parents/Children_Aboard':'Parent_Children_Aboard'},inplace=True)

pg_conn = pg2.connect(dbname = DBNAME, user= USER, password= PASSWORD,host= HOST)
pg_curs = pg_conn.cursor()

pg_curs.execute("CREATE TABLE IF NOT EXISTS titanic(\
    survived INT NOT NULL,\
    pclass INT NOT NULL,\
    name VARCHAR(90) NOT NULL,\
    sex VARCHAR(10) NOT NULL,\
    age FLOAT NOT NULL,\
    sibling_spouse_aboard INT NOT NULL,\
    parent_children_aboard INT NOT NULL,\
    fare FLOAT NOT NULL\
)")



for index,row in df.iterrows():
    pg_curs.execute("INSERT INTO titanic (\
        survived,pclass,name,sex,age,sibling_spouse_aboard,parent_children_aboard,fare)\
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (row.Survived,row.Pclass,row.Name,row.Sex,row.Age,row.Sibling_Spouse_Aboard,
        row.Parent_Children_Aboard,row.Fare))

pg_conn.commit()
# pg_curs.close()

pg_curs.execute("SELECT * FROM titanic;")
rows = pg_curs.fetchall()

pg_curs.close()
print(rows)



