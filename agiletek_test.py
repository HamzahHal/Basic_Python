import pandas as pd
# importing the requests library
import requests


def read_data():
    dataset = pd.read_csv('coding_exam.csv')
    return dataset


print(read_data())


def api():
    try:

        API_ENDPOINT = "https://api.agiletek.co.uk/cps%60"

        API_KEY = "58791d45aa40fa2508bccd57"

         # data to be sent to api
        data = {'api_dev_key': API_KEY,
            'api_option': 'paste',
            'api_paste_format': 'python'}

        # sending post request and saving response as response object
        r = requests.post(url=API_ENDPOINT, data=data)

        # extracting response text
        pastebin_url = r.text
        print("The pastebin URL is:%s" % pastebin_url)
    except requests.exceptions:
        print("ApI ISSUES")


print(api())
