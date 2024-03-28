#!/usr/bin/python3
"""print Error """
import urllib.request
from urllib.error import HTTPError
import sys


try:
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
        print(html)
except urllib.error.HTTPError as e:
    if hasattr (e, 'code'):
        print ("Error code:", e.code)
except:
    pass
