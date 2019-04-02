#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests


URL_BASE = "http://api.openweathermap.org/data/2.5/forecast?"
LAT = "35.543251"
LON = "139.517218"
KEY = "d171c64bee9ad5febbba628f6e1b46b7"
# 経度(LAT)と緯度(LON)で位置を指定している。とりあえず横浜市青葉区の青葉台駅に設定した
# print(URL_BASE + "lat=" +  LAT + "&lon=" + LON  + "&appid=" + KEY)

response = requests.get(URL_BASE + "lat=" +  LAT + "&lon=" + LON  + "&appid=" + KEY).json()
jsontext = json.dumps(response, indent=2)

# print(jsontext)

data = json.loads(jsontext)

print("現在の風速：" + str(data["wind"]["speed"]) + "m")
print("対象の都市は" + data["city"]["name"] + "です")