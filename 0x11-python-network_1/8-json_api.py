#!/usr/bin/python3
'''Sends a POST request to an email'''

import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if sys.argv[1]:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    r = requests.post(url, data={'q': sys.argv[1]})
    try:
        r.json()
        print("[{}] {}".format(r.headers.get('id'), r.headers.get('name')))
    except:
        if r.status_code == 204:
            print("No result")
        else:
            print("Not a valid JSON")
