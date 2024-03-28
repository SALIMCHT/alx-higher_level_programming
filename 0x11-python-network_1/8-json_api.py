#!/usr/bin/python3
""" With request ask for header"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        data = {'q': ""}
    else:
        data = {'q': sys.argv[1]}
    html = requests.post(url, data)
    try:
        my_json = html.json()
        if len(my_json) is 0:
            print("No result")
        else:
            print("[{}] {}".format(my_json.get('id'), my_json.get('name')))
    except BaseException:
        print("Not a valid JSON")
