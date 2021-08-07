import pandas as pd
from urllib.request import urlopen
import json
import csv


def import_data():
    with open('coding_exam.csv', mode='r') as infile:
        reader = csv.reader(infile)
        with open('coding_new.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            mydict = {rows[0]: rows[1] for rows in reader}
            return mydict


def read_data():
    Dataframe = pd.read_csv("coding_exam.csv")
    return Dataframe


def api():
    dataset = pd.read_json('coding_exam.json')
    new_data = {"Project Code": dataset.iloc[0:4], "cps model number": dataset.iloc[1:4], "pile_x": dataset.iloc[2:4],
                "pile_y": dataset.iloc[3:4], "pile_z": dataset.iloc[4:4], "cable_mg_thickness": dataset.iloc[5:4],
                "cable mg width": dataset.iloc[6:4], "cable mg length": dataset.iloc[6:4]}

    # dictionary = {k: None for k in new_data}
    df = pd.DataFrame(list(new_data.items()), columns=["Project Code", "cps model number",
                                                       "pile_x", "pile_y",
                                                       "pile_z", "cable_mg_thickness",
                                                       "cable mg width", "cable mg length"])

    # dictionary["Project Code"] = dataset.iloc[0, 0]
    # dictionary["Project Code"] = dataset.iloc[0]

    return df


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
print(import_data())