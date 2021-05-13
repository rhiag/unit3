"""Pipeline to move data from csv to MongoDB"""

import pandas as pd
import pymongo

PASSWORD = "BVIsO0ZO1GRSDnnr"
DBNAME = "myFirstDatabase"

FILENAME = "https://raw.githubusercontent.com/LambdaSchool/data-science-practice-datasets/main/unit_1/Titanic/Titanic.csv"



def connect_to_mongo(password,dbname):
    #Client that connects to MongoDB cluster
    client = pymongo.MongoClient(
        "mongodb+srv://rhiag-UbuntuOS:{}@cluster0.1bqaf.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
        )
    return client

def csv_to_doc(filename, header=None):
    """
    Function to read csv in a dataframe.
    Use pandas .to_dict() function to convert dataframe to dict of series
    Each column is a series and thus returns a dictionary of series
    """
    df = pd.read_csv(filename)
    df.rename(columns= {'Siblings/Spouses_Aboard':'Sibling_Spouse_Aboard','Parents/Children_Aboard':'Parent_Children_Aboard'},inplace=True)
    return df.to_dict('records')


if __name__ == "__main__":
    mongo_client = connect_to_mongo(PASSWORD,DBNAME)
    collection = mongo_client.myFirstDatabase.myFirstDatabase
    collection.delete_many({})
    print(csv_to_doc(FILENAME))
    count_before_insert = collection.count_documents({})
    collection.insert_many(csv_to_doc(FILENAME, header=0))
    count_after_insert =  collection.count_documents({})
    print("----------------------------------------------")
    print("Count before insert into collection:",count_before_insert)
    print("Count after insert into collection:",count_after_insert)
    print("-------------------------------------------------")  