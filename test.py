import requests
import os
import pandas as pd
from orjson import orjson


def get_testData():

    df=pd.read_csv("C:\\Users\\MCS\\Downloads\\diabetes.csv")
    #temp = df.loc[:, ["Pregnancies", "Glucose", "Insulin", "Age"]].to_json(orient='records')
    # creates json dumps
    #temp = orjson.loads(temp)
    #dp=requests.get(temp).json()
    #return dp

if __name__ == "__main__":
    temp=get_testData()
