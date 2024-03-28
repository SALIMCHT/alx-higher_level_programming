#!/usr/bin/python3
""" With request ask for header"""
import requests
import sys

if __name__ == "__main__":
    url = "http://swapi.co/api/people/?all=true"
    url2 = "http://swapi.co/api/films/"
    if len(sys.argv) < 2:
        sys.exit(1)
    else:
        data = {'search': sys.argv[1]}
    html = requests.get(url, params=data)
    try:
        my_json = html.json()
        print("Number of results: ", my_json.get('count'))
        list_results = my_json.get('results')
        for dict_results in list_results:
            print(dict_results.get('name'))
            full_html2 = url2 + "?search={}".format(dict_results.get('name'))
            print(full_html2)
            html2 = requests.get(url2 + "?search={}".format(dict_results.get('name')))
            my_json2 = html2.json()
            print(my_json2)
    except:
        pass
