import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
import re

class IncorrectData(Exception):
    pass

class HelperFunctions:
    """
    This class is used to clean up the code
    """

    def __init__(self):

        """
        Constructor class for HelperFunctions
        """
        pass
        

    def null_count(self,data):
        """
        This method returns the number of null values in a Dataframe
        """
        df = pd.DataFrame(data)
        if data == None:
            raise IncorrectData(
                "Check for None"
            )
        else:
            return df.isnull().sum().sum()


    def train_test_split(self,data,frac):
        """
        This method splits the data using train_test_splt and returns both training and testing set
        """
        df = pd.DataFrame(data)
        train,test = train_test_split(df,train_size =frac,random_state =42)
        return (train,test)


    def split_dates(self ,date_series):
        """Splits date into month day and year"""
        df = pd.Dataframe()
        df['date'] = date_series
        df[["day", "month", "year"]] = df['date'].str.split("/", expand = True)
        df.drop(columns = 'date',inplace = True)
        return df

        

if __name__ == "__main__":
    data = ([None, 72, 67],
	        [23, 78, 62],
	        [32, 74, None],
	        [None, 54, 76])

    helper = HelperFunctions()        
    count= helper.null_count(data)        
    print(count)


    
