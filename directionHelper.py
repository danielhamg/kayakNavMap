def directionCheck(ahmetPosition, ship):
    oldLat = getLatShip(ship)
    oldLon = getLonShip(ship)
    newLat = predictNextLatLon(ship, getShipTimeStamp(ship))[0]
    newLon = predictNextLatLon(ship, getShipTimeStamp(ship))[1]
    if distanceCalculator(ahmetPosition.lat, ahmetPosition.lon, newLat, newLon) < distanceCalculator(ahmetPosition.lat, ahmetPosition.lon, oldLat, oldLon):
        return true
    return false
