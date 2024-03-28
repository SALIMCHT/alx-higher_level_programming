#!/usr/bin/python3
""" With request ask for header"""
import requests
import sys

try:
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}
    html = requests.post(url, data=params)
    print(html.text)
except:
    pass
