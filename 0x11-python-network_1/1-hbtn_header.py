#!/usr/bin/python3
"""request a specific header """
import urllib.request
import sys

try:
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.getheader("X-Request-Id")
        print(html)
except:
    pass
