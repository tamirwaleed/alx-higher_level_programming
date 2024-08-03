#!/usr/bin/python3
'''X-Request-Id variable found in the header of the response'''

import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(dict(r.headers).get('X-Request-Id'))
