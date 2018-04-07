class AllData:
	def __init__(self, file):
		# array file
		self.file = file
		self.switcher = {
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

	def getIndex(self, id):
		return self.switcher[id]

	# gets a ship item at index
	def getShipItem(self, index, item):
		return self.file[index][self.switcher[item]]