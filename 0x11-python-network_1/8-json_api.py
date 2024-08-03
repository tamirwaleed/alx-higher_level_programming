#!/usr/bin/python3
'''Sends a POST request to an email'''

import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        r = requests.post(url, data={'q': sys.argv[1]})
    else:
        r = requests.post(url, data={'q': ""})
    try:
        r = r.json()
        print("[{}] {}".format(r.headers.get('id'), r.headers.get('name')))
    except:
        if r.status_code == 204:
            print("No result")
        else:
        print("Not a valid JSON")
