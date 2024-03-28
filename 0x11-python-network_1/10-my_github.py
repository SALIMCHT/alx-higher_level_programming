#!/usr/bin/python3
""" With request ask for header"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    if len(sys.argv) < 3:
        sys.exit(1)
    else:
        auth = (sys.argv[1], sys.argv[2])
        html = requests.get(url, auth=auth)
        my_json = html.json()
        try:
            print(my_json.get('id'))
        except:
            pass
