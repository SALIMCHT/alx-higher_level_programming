#!/usr/bin/python3
""" With request ask for header"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(1)
    else:
        url = 'https://api.github.com/repos/{}/{}/commits'.\
            format(sys.argv[1], sys.argv[2])
        html = requests.get(url)
        my_json = html.json()
        for member_list in my_json[:10]:
            print("{}: {}".format(member_list.get('sha'),
                                  member_list.get('commit').get('author').
                                  get('name')))
