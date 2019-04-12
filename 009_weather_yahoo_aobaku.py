#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

# Yahoo天気で現在の気象情報を表示する

URL_BASE = "https://map.yahooapis.jp/weather/V1/place?coordinates="
LAT = "35.543251"
LON = "139.517218"
KEY = "dj00aiZpPVdxWGtKZm5DMXRWWCZzPWNvbnN1bWVyc2VjcmV0Jng9ZWU-"
# 経度(LAT)と緯度(LON)で位置を指定している。とりあえず横浜市青葉区の青葉台駅に設定した
# print(URL_BASE + "lat=" +  LAT + "&lon=" + LON  + "&appid=" + KEY)

response = requests.get(URL_BASE + LON + "," + LAT  + "&appid=" + KEY).json()
jsontext = json.dumps(response, indent=2)

# print(jsontext)

data = json.loads(jsontext)

print("現在の風速：" + str(data["wind"]["speed"]) + "m")
print("対象の都市は" + data["name"] + "です")
