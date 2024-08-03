#!/usr/bin/python3
'''Sends a POST request to an email'''

import requests
import requests.auth
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    pswd = sys.argv[2]
    url = 'https://api.github.com/user/' + username
    r = requests.get(url,
                     auth=HTTPBasicAuth(username, pswd))
    print(r.json().get('id'))
