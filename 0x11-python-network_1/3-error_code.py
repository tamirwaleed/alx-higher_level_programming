#!/usr/bin/python3
'''Python script that sends a request to the URL and 
and displays the response body'''


import sys
import urllib.parse
import urllib.request
import urllib.error.HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(e.reason)
