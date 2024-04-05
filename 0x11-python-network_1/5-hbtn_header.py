#!/usr/bin/python3

""" takes in a URL, sends a request to the URL and displays the value."""

import sys
import requests


if __name__ == "__main__":

    cmdURL = sys.argv[1]
    response = requests.get(cmdURL)
    X_Request_Id = response.headers["X-Request-Id"]
    print(X_Request_Id)
