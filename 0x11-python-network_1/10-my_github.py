#!/usr/bin/python3
'''Sends a POST request to an email'''

import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    pswd = sys.argv[2]
    data={'username': username, 'password': pswd}
    r = requests.post(url, data=data)
    print(r.json().get('id'))
