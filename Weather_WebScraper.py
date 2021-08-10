from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

url = 'https://forecast.weather.gov/MapClick.php?lat=' + 'latitude' + '&long=' + 'longitude'
page = requests.get(url)
print(page)
