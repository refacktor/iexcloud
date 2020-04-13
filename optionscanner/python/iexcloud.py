import json
import os
import argparse
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument('--config', help='path to config file')
parser.add_argument('--stock', help='stock symbol')
args = parser.parse_args()

with open(args.config, "r") as f:
    config = json.loads(f.read())
    
sk = config['secretKey']
pk = config['publishableKey']
baseUrl = config['baseUrl']

def get(api):
    url = baseUrl + api + "?token=" + config['secretKey']
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())
    
expirationDates = get('/stock/%s/options' % args.stock)

for expiration in expirationDates[:1]:
    print(expiration)
    data = get('/stock/%s/options/%s' % (args.stock, expiration))
    print(data)