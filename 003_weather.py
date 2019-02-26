#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import requests

def wether_inf():
	url = "http://api.openweathermap.org/data/2.5/weather?q=Tokyo"
	response = requests.get(url).json()
	jsontext = json.dumps(response, indent=2)
	print(jsontext)
	
	wind1 = response[``]

	return response
