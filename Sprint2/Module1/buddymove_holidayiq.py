import pandas as pd
import sqlite3

url = "https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv"

df = pd.read_csv(url)
print(df.shape)

# Step1 :  Connect to Database
conn = sqlite3.connect("../data/buddymove_holidayiq.sqlite3")
curs = conn.cursor()

#Step2: Create database
curs.execute("CREATE TABLE review (User Id,Sports,\
                Religious,Nature,Theatre,Shopping,Picnic)")
conn.commit()

#Step 3: Writes records stored in df to a SQL database 'review'.
df.to_sql('review', con = conn, if_exists ='replace', index=False)

#Step3: SQL Queries to test
rows = curs.execute("SELECT count(*) FROM review;").fetchall()
nature_reviews = curs.execute("SELECT COUNT(*) FROM review\
                                WHERE Nature > 100 AND Shopping > 100;").fetchall()
avg_per_category = curs.execute("select avg(sports),avg(Religious),avg(nature),avg(theatre),avg(shopping),avg(picnic) from review;").fetchall()
#Step4: Print Results
print("Rows:",rows)
print("Views of nature and shopping:", nature_reviews)
print("Averages:",avg_per_category)




