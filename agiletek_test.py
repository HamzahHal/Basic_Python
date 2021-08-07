import numpy as np
import pandas as pd
import requests
from requests.structures import CaseInsensitiveDict
# import urllib library
from urllib.request import urlopen
# import json
import json


def read_data():
    Dataframe = pd.read_csv("coding_exam.csv")
    return Dataframe

def api():
    dataset = pd.read_csv('coding_exam.csv')
    post_data = {}
    post_data["Project Code"] = dataset.iloc[0,0]
    return post_data


try:
    # store the URL in url as
    # parameter for urlopen
    url = "https://api.agiletek.co.uk/cps%60"

    # store the response of URL
    response = urlopen(url)

    # storing the JSON response
    # from url in data
    data_json = json.loads(response.read())

    # print the json response
    print(data_json)
except:
    print("not working")



print(read_data())
print(api())


