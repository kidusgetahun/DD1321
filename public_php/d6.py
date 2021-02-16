import json
import urllib
import urllib.request
import sys

schemaurl = "https://www.kth.se/social/api/schema/v2/course/"
course = "DD1321"
start = "?startTime=2020-01-14"
schemaurl += course + start

request_data = urllib.request.urlopen(schemaurl).read() # hämtar data från REST-servern
utf_data = request_data.decode('utf-8')                 # översätter u00f6 -> ö
datastruktur = json.loads(utf_data)                     # lägger in i en pythonstruktur

print(datastruktur["entries"][2])
print(datastruktur["entries"][2]["start"])
print(datastruktur["entries"][2]["end"])
print(datastruktur["entries"][2]["title"])
for x in datastruktur["entries"][2]["locations"]:
    print(x["name"])