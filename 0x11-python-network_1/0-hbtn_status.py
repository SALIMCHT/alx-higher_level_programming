#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
a = type(html)
b = html.decode("utf-8")
print("Body response:")
print("\t- type: {}".format(a))
print("\t- content: {}".format(html))
print("\t- utf8 content: {}".format(b))
