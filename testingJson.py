from requests import get
from dataSave import *
import json


# 
file = get("https://services.marinetraffic.com/api/exportvessels/v:8/2bede1ff947de189f635a8781c0d606b455f61b4/timespan:2/protocol:json")

jsonObj = json.loads(file.text)




currentFile = AllData(jsonObj)
print(currentFile.getShipItem(1, "MMSI"))