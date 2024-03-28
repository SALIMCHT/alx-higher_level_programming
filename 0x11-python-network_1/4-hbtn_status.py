#!/usr/bin/python3
""" With request"""
import requests
html = requests.get('https://intranet.hbtn.io/status')
a = type(html.text)
print("Body response:")
print("\t- type: {}".format(a))
print("\t- content: {}".format(html.text))
