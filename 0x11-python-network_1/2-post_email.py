#!/usr/bin/python3
"""send email ans look the return """
import urllib.request
import urllib.parse
import sys

try:
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}
    query_string = urllib.parse.urlencode(params)
    data = query_string.encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        html = response.read().decode("utf-8")
        print(html)
except:
    pass
