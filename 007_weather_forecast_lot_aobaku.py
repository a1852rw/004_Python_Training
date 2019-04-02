#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests
from datetime import datetime

# 3時間ごとの天気予報をまとめて出力するプログラム

URL_BASE = "http://api.openweathermap.org/data/2.5/forecast?"
LAT = "35.543251"
LON = "139.517218"
KEY = "d171c64bee9ad5febbba628f6e1b46b7"
# 経度(LAT)と緯度(LON)で位置を指定している。とりあえず横浜市青葉区の青葉台駅に設定した

# print(URL_BASE + "lat=" +  LAT + "&lon=" + LON  + "&appid=" + KEY)

response = requests.get(URL_BASE + "lat=" +  LAT + "&lon=" + LON  + "&appid=" + KEY).json()
jsontext = json.dumps(response, indent=4)
data = json.loads(jsontext)

#print(jsontext)

for item in data['list']:
	windData = item["wind"]["speed"]
	timeData = item["dt_txt"]
	print(str(timeData) + " の風速は " + str(windData) + "m/s です")
	break

print("対象の都市は" + data["city"]["name"] + "です")
