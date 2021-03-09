#!/usr/bin/python3

import requests, random, sys

data = {}
data['V'] = random.randrange(4096)  # random voltage
data['I'] = random.randrange(4096)  # random current
data['pi'] = 3.14   

if len(sys.argv) >= 2:
    hostname = sys.argv[1]
else:
    hostname = 'localhost'

url = "http://%s:8080/sciota/footprint" % hostname

response = requests.post(url, data)
print(response)
