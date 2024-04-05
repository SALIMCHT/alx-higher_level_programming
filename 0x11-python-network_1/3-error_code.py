#!/usr/bin/python3

""" takes in a URL, sends a request to the URL and displays the value."""

import sys
import urllib.request


if __name__ == "__main__":
    URL = sys.argv[1]
    try:
        # reqObj = urllib.request.Request(URL)
        with urllib.request.urlopen(URL) as response:
            content = response.read()
            print(content.decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
