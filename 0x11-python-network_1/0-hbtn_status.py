#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request
if __name__ == "__main__":
    Url0 = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(Url0)

    with urllib.request.urlopen(req) as response:
        # Displaying information about the response body
        res = response.read()
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode("utf-8")))
