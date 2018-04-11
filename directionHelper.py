def directionCheck(ahmetPosition, ship):
    oldLat = getLatShip(ship)
    oldLon = getLonShip(ship)
    newLat, new Lon = predictNextLatLon(ship, getShipTimeStamp(ship))
    if distanceCalculator(ahmetPosition.lat, ahmetPosition.lon, newLat, newLon) < distanceCalculator(ahmetPosition.lat, ahmetPosition.lon, oldLat, oldLon):
        return true //towards
    return false





predictNextLatLon(ship, getShipTimeStamp(ship))
