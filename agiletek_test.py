import pandas as pd
import json
import csv


def read_data():
    data_set = dict(pd.read_json("coding_exam.json"))
    columns = data_set.keys()
    rows = data_set.items()
    new_type = (columns, rows)
    return new_type


def api():
    dataset = pd.read_json('coding_exam.json')
    new_data = {"Project Code": dataset.iloc[0, 1], "cps model number": dataset.iloc[1:4], "pile_x": dataset.iloc[2:4],
                "pile_y": dataset.iloc[3:4], "pile_z": dataset.iloc[4:4], "cable_mg_thickness": dataset.iloc[5:4],
                "cable mg width": dataset.iloc[6:4], "cable mg length": dataset.iloc[6:4]}

    new_data = {k: None for k in new_data}
    # df = pd.DataFrame(list(new_data.items()), columns=["Project Code", "cps model number",
    #                                                   "pile_x", "pile_y",
    #                                                   "pile_z", "cable_mg_thickness",
    #                                                   "cable mg width", "cable mg length"])

    # dictionary["Project Code"] = dataset.iloc[0, 0]
    # dictionary["Project Code"] = dataset.iloc[0]

    return new_data


print(read_data())

# with open('coding_exam.json','r') as f:
# aList = json.dumps(dataset)
# data = json.load()
# data = json.loads(f.read())
# df_nested_list = pd.json_normalize(data, record_path=["alProject Code"])
