class Ships:

    # Ship Fields: Corresponding to JSON file from Marine Traffic API
    fields = {
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

    # Constructor: takes in JSON file
    def __init__(self, file):
        self.allShips = file

    # Returns a tuple of predicted longitude and latitude (in that order)
    def predictNextLatLon(ship, nexTime):
        speedX = knotsToMps(cos(getSpeedShip(ship)))
        speedY = knotsToMps(sin(getSpeedShip(ship)))
        diffTime = timeDifferenceSeconds(getTimeShip(ship), nexTime)
        diffX = mtoCoor(speedX * diffTime)    # should be in coor
        diffY = mtoCoor(speedY * diffTime)    # should be in coor
        newLon = getLonShip(ship) + diffX
        newLat = getLatShip(ship) + diffY
        return [newLon, newLat]


    ######################################################
    ################## HELPER FUNCTIONS ##################
    ######################################################

    # Gets the output of a particular ship's field; General helper function
	def getShipField(self, shipIndex, field):
		item = item.upper()
		return self.allShips[index][fields[item]]

    # Get a ship's ID
    def getShipId(self, shipIndex):
        return int(self.getShipfield(index, "SHIP_ID"))

	# Get a ship's latitude
	def getLatShip(self, shipIndex):
		return int(self.getShipField(index, "LAT"))

	# Get a ship's longtitude
	def getLonShip(self, shipIndex):
		return int(self.getShipField(index, "LON"))

	# Get a ship's heading
	def getHeadingShip(self, shipIndex):
		return int(self.getShipField(index, "HEADING"))

    def getSpeedShip(ship):
        return float(getShipField(ship, "SPEED"))

    def getSpeedTimeStamp(ship):
        return getShipField(ship, "TIMESTAMP")

    def timeStampCompress(stamp):
        indexT = stamp.find('T')
        return stamp[indexT + 1:]

    def getTimeShip(ship):
        return timeStampCompress(getSpeedTimeStamp(ship))

    def timeDifferenceSeconds(before, after):
        FMT = '%H:%M:%S'
        return (datetime.strptime(after, FMT) - datetime.strptime(before, FMT)).total_seconds()

    def knotsToMps(knots):
        return knots / 0.51444444444

    def mtoCoor(m):
        return m / 1852
