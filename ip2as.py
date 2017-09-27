#!/usr/bin/python
#
#IP2AS.py
#Script to Get AS number from IP address

import requests

hit=0

prefix = input("Enter IP Prefix: ")
print ("looking for:",prefix)

res = requests.get("http://ftp.ripe.net/ripe/stats/delegated-ripencc-latest")

mad = res.text
#print(mad.find(prefix))

for item in mad.split("\n"):
    if "|"+prefix in item:
        print (item.strip())
        matchline = (item.strip())
        print ("Input:",prefix,"Prefix",matchline.split("|")[3],"AS Number: AS",matchline.split("|")[4])
        hit += 1
        break

if hit == 0:
    print ("Sorry no match for ",prefix)
