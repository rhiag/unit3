"""Collection of Helper_functions"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
import re

print("Inside the helper_function")

def null_count(df):
    """This functions returns the number of null values in a Dataframe"""
    return df.isnull().sum().sum()


def train_test_split(df,frac):
    """This function splits the data using train_test_splt and returns both training and testing set"""
    train,test = train_test_split(df,train_size =frac,random_state =42)
    return (train,test)


def randomize(df, seed):
    """Randomizes all the cells in a dataframe"""
    df_randomized = shuffle(df, random_state= seed)
    return df_randomized

    
def split_dates(date_series):
    """Splits date into month day and year"""
    df = pd.Dataframe()
    df['date'] = date_series
    df[["day", "month", "year"]] = df['date'].str.split("/", expand = True)
    df.drop(columns = 'date',inplace = True)
    return df

def addy_split(addy_series):
    """Splits address into 3 columns of city,state and zip"""
    
    address = addy_series
    add = pd.DataFrame(columns=['city','state','zip'])
    city =[]
    state=[]
    zipcode=[]

    for address in address_list: 
        result = re.match(r'^.*\n(?P<city>[\w\s]+),\s(?P<state>[A-Z]{2})\s(?P<zip>\d+)$',address)
        city.append(result.group('city'))
        state.append(result.group('state'))
        zipcode.append(result.group('zip'))
    
    add['city'] = city
    add['state'] = state
    add['zip'] = zipcode

    return add




    
