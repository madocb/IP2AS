#Script to Get AS number from IP address
#In Development

import requests

prefix = input("Enter IP Prefix:")
print ("looking for:",prefix)

res = requests.get("http://ftp.ripe.net/ripe/stats/delegated-ripencc-latest")

mad = res.text
print(mad.find(prefix))

for item in mad.split("\n"):
    if "|"+prefix in item:
        print (item.strip())
        break
