#!/usr/bin/python3
'''Retrieve 10 last commits'''

import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    repna = sys.argv[1]
    ownna = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(ownna, repna)
    r = dict(requests.get(url).json())
    print(type(r))
