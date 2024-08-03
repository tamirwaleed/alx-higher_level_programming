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
        if len(r) > 0 and r.get('id') and r.get('name'):
            print("[{}] {}".format(r.get('id'), r.get('name')))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
