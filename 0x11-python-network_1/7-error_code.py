#!/usr/bin/python3
""" With request ask for header"""
import requests
import sys

try:
    url = sys.argv[1]
    html = requests.get(url)
    status = int(html.status_code)
    if status >= 400:
        print("Error code: ", status)
    else:
        print(html.text)
except:
    pass
