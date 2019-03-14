#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
from datetime import datetime

URL_BASE = "http://api.openweathermap.org/data/2.5/forecast?"
LAT = "35.266084"
LON = "139.147338"
KEY = "d171c64bee9ad5febbba628f6e1b46b7"
# 経度(LAT)と緯度(LON)で位置を指定している。とりあえず小田原近くに設定した

print(URL_BASE + "lat=" +  LAT + "&lon=" + LON  + "&appid=" + KEY)

response = requests.get(URL_BASE + "lat=" +  LAT + "&lon=" + LON  + "&appid=" + KEY).json()
jsontext = json.dumps(response, indent=4)
data = json.loads(jsontext)

print(jsontext)

#for item in data['list']:
#	windData = item["wind"]["speed"]
#	timeData = item["dt_txt"]
#	print(str(timeData) + " の風速は " + str(windData) + "m/s です")
#	break

#for item in date["city"]:
#	cityName = item["name"]
#	print(cityName)
#	break
