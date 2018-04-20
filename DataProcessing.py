class DataProcessing:
	# Radius Filter: Returns a list of ships that are within the radius of 125m
    def withinRadiusShips(ships, ahmet):
    	withinRadiusShips = []
    	for i in ships.allShips:
    		if booleanWithinRadius(i, ahmet):
    			withinRadiusShips.append(i)
    	return withinRadiusShips

    # Direction Filter: Returns a tuple of ships moving towards Ahmet, and ships moving away
    def withinDirectionShips(withinRadiusShips, ahmet):
        shipsTowards = []
        shipsAway = []
        for i in withinRadiusShips:
            if directionCheck(i, ahmet):
                shipsTowards.append(i)
            else:
                shipsAway.append(i)
        return (shipsTowards, shipsAway)

    ######################################################
    ################## HELPER FUNCTIONS ##################
    ######################################################

    # Returns true if ship is within radius; false otherwise
    def booleanWithinRadius(ship, ahmet):
    	lonS = ship.getLonShip
        latS = ship.getLatShip
        lonAhmet = Ahmet.getLonShip
    	latAhmet = Ahmet.getLatShip
    	if (distanceCalculator(lonS, latS, lonAhmet, latAhmet) > 125):
    		return false
    	return true

    # Returns the distance between ship and Ahmet
    # Source: https://stackoverflow.com/questions/639695/how-to-convert-latitude-or-longitude-to-meters
    def distanceCalculator(lon1, lat1, lon2, lat2):
        R = 6378.137
        dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180
        dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
        a = math.sin(dLat / 2) * math.sin(dLat / 2)
        + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180)
        * math.sin(dLon/2) * math.sin(dLon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c
        return d * 1000

    # Returns true if ship is travelling towards Ahmet; false otherwise
    def directionCheck(ship, ahmet):
        oldLat = getLatShip(ship)
        oldLon = getLonShip(ship)
        newLat = predictNextLatLon(ship, getShipTimeStamp(ship))[0]
        newLon = predictNextLatLon(ship, getShipTimeStamp(ship))[1]
        if distanceCalculator(ahmetPosition.lon, ahmetPosition.lat, newLon, newLat)
        < distanceCalculator(ahmetPosition.lon, ahmetPosition.lat, oldLon, oldLat):
            return true
        return false
