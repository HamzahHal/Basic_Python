import csv
import sys
import json
from collections import OrderedDict


def parseCSV(data):
    types = ["str", "str", "float", "float", "float", "float", "float", "float", "float"]
    keys = [k.replace(" ", "_").lower() for k in data[0]]
    converted = []
    for i in range(1, len(data)):
        obj = OrderedDict()
        for j in range(0, len(keys)):
            try:
                if len(data[i][j]) > 0:
                    if types[j] == "float":
                        obj[keys[j]] = float(data[i][j])
                    else:
                        obj[keys[j]] = data[i][j]
                else:
                    obj[keys[j]] = None
            except:
                obj[keys[j]] = None
        converted.append(obj)
    return converted


def createOutputJSON(data):
    jsonfile = open("output.json", "w")
    jsonfile.write(json.dumps(data, indent=4))


def addVolume(data):
    success = csv.writer(open("success.csv", "w"))
    fail = csv.writer(open("fail.csv", "w"))
    success.writerow(data[0].keys())
    fail.writerow(data[0].keys())

    for i in range(len(data)):
        data_values = data[i].values()
        data[i]["project_code"] = "TEK-" + data[i]["project_code"]

        if None in data_values:
            fail.writerow(data_values)

        else:
            data[i]["cable_mg_volume"] = (
                data[i]["cable_mg_thickness"] + data[i]["cable_mg_width"] + data[i]["cable_mg_length"]
            )
            success.writerow(data[i].values())

    json.dump(data, open("output.json", "w"), indent=4)


def main():
    try:
        filename = sys.argv[1]
        file_format = filename.split(".")[-1].lower()
        file = open(sys.argv[1])
        if file_format == "csv":
            res = parseCSV(list(csv.reader(file)))
            createOutputJSON(res)
            addVolume(json.load(open("output.json", "r")))
        else:
            exit()
    except TypeError as e:
        print(e)
        print("You must provide a valid csv file")


main()