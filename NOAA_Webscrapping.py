# needed to make web requests
import requests
# store the data we get as a dataframe
import pandas as pd

# convert the response as a strcuctured json
import json

# mathematical operations on lists
import numpy as np

# parse the datetimes we get from NOAA
from datetime import datetime

from bs4 import BeautifulSoup

# add the access token you got from NOAA
Token = 'cnlrSvGHZSQIfiwenhDmDGFdsPAwHemn'
station_id = 'GHCND:USW00013958' # # Station Id

dates_temp = []
dates_prcp = []
temps = []
prcp = []

# for each year from 2015-2019 ...
for year in range(2019, 2020):
    year = str(year)
    print('working on year ' + year)

    # make the api call
    r = requests.get(
        'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TAVG&limit=1000&stationid=GHCND:USW00013958&startdate=' + year + '-01-01&enddate=' + year + '-12-31',
        headers={'token': Token})
    # load the api response as a json
    d = json.loads(r.text)
    # get all items in the response which are average temperature readings
    avg_temps = [item for item in d['results'] if item['datatype'] == 'TAVG']
    # get the date field from all average temperature readings
    dates_temp += [item['date'] for item in avg_temps]
    # get the actual average temperature from all average temperature readings
    temps += [item['value'] for item in avg_temps]



"""
soup = BeautifulSoup(r.content, "html.parser")
    all = soup.find("div", {"class": "locations-title ten-day-page-title"}).find("h1").text
    table = soup.find_all("table", {"class": "twc-table"})
    l = []
    for items in table:
        for i in range(len(items.find_all("tr")) - 1):
            d = {}
            d["day"] = items.find_all("span", {"class": "date-time"})[i].text
            d["date"] = items.find_all("span", {"class": "day-detail"})[i].text
            d["desc"] = items.find_all("td", {"class": "description"})[i].text
            d["temp"] = items.find_all("td", {"class": "temp"})[i].text
            d["precip"] = items.find_all("td", {"class": "precip"})[i].text
            d["wind"] = items.find_all("td", {"class": "wind"})[i].text
            d["humidity"] = items.find_all("td", {"class": "humidity"})[i].text
            l.append(d)
    
"""