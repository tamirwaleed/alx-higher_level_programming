#!/usr/bin/python3
'''Retrieve 10 last commits'''

import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    repna = sys.argv[1]
    ownna = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(ownna, repna)
    r = requests.get(url)
    for x in r.json()[:10]:
        print("{}: {}".format(x.get("sha"),
                              x.get('commit').get('author').get('name')))
