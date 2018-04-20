class Ships:

    fields = {
		"MMSI" : 0,
		"IMO" : 1,
		"SHIP_ID" : 2,
		"LAT" : 3,
		"LON" : 4,
		"SPEED" : 5,
		"HEADING" : 6,
		"COURSE" : 7,
		"STATUS" : 8,
		"TIMESTAMP" : 9,
		"DSRC" : 10,
		"UTC_SECONDS" : 11
	}

    def __init__(self, file):
        self.allShips = file

	def getShipField(self, shipIndex, item):
		item = item.upper()
		return self.allShips[index][fields[item]]

	# get a ship's latitude
	def getLatShip(self, shipIndex):
		return int(self.getShipField(index, "lat"))

	# get a ship's longtitude
	def getLonShip(self, shipIndex):
		return int(self.getShipField(index, "lon"))

	# get a ship's heading
	def getHeadingShip(self, shipIndex):
		return int(self.getShipField(index, "heading"))

	# update relevants with which ships are relevant to him
	def updateRelevants(self):
		relevants = DataProcessing.updateRelevantShips(radius)





	# Filter out ships that are away from Ahmet, and are going away from him anyways
	def filterNonrelevant(self):
		def upAndMovingAway(lat, heading):
			return lat > self.lat and
		for ship in allShips:
			if ((getLatShip > self.lat and (heading < 60)))


		# REPLACE
		return none










file = get("https://services.marinetraffic.com/api/exportvessels/v:8/2bede1ff947de189f635a8781c0d606b455f61b4/timespan:2/protocol:json")
jsonObj = json.loads(file.text)

ahmet = Ahmet(jsonObj, lat, lon)

print(ahmet.getShipItem(1, "MMSI"))
