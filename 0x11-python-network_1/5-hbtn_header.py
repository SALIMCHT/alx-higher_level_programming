#!/usr/bin/python3
""" With request ask for header"""
import requests
import sys

try:
    url = sys.argv[1]
    html = requests.get(url)
    a = html.headers["X-Request-Id"]
    print(a)
except:
    pass
