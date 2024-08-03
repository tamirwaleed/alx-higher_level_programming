#!/usr/bin/python3
''' Write a Python script that fetches https://alx-intranet.hbtn.io/status '''

import requests


url = 'https://alx-intranet.hbtn.io/status'
r = requests.get(url)
print('Body response:\n\t- type: {}'.format(type(r)))
print('\t- content: {}'.format(r))
