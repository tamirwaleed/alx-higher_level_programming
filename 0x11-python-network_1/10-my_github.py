#!/usr/bin/python3
'''Log into GitHub'''

import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    pswd = sys.argv[2]
    url = 'https://api.github.com/user/' + username
    r = requests.get(url,
                     auth=HTTPBasicAuth(username, pswd))
    print(r.json().get('id'))
