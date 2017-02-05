#!/usr/bin/env python

import requests

base_url = 'http://127.0.0.1:5000'
api_version = 'v1.0'
lang = 'en'

resp = requests.get(base_url + '/' + api_version + '/' + lang + '/hymn/1')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))

print resp.json()
