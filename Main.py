from requests import get
import json


file = get("https://services.marinetraffic.com/api/exportvessels/v:8/2bede1ff947de189f635a8781c0d606b455f61b4/timespan:2/protocol:json")
jsonObj = json.loads(file.text)

ahmet = Ahmet(jsonObj, lat, lon)

print(ahmet.getShipItem(1, "MMSI"))
