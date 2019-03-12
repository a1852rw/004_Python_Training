#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

URL_BASE = "http://api.openweathermap.org/data/2.5/forecast?q="
URL_CITY = "Tokyo"
KEY = "d171c64bee9ad5febbba628f6e1b46b7"

# print(URL_BASE + URL_CITY + "&appid=" + KEY)

response = requests.get(URL_BASE + URL_CITY + "&appid=" + KEY).json()
jsontext = json.dumps(response, indent=4)
data = json.loads(jsontext)

# print(jsontext)
for item in data['list']:
	windData = item["wind"]["speed"]
	timeData = item["dt_txt"]
	print(windData)
	print(timeData)
	break
