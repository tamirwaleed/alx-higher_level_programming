#!/usr/bin/python3
''' Write a Python script that fetches https://alx-intranet.hbtn.io/status '''

import requests


url = 'https://alx-intranet.hbtn.io/status'
resp = requests.get(url)
r = resp.read()
print('Body response:\n\t- type: {}'.format(type(r)))
print('\t- content: {}'.format(r))
