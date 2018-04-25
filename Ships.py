class Ships:

    # Ship Fields: Corresponding to JSON file from Marine Traffic API
    #################################
    # Previously under Ships class. Now will be simplified to only take in a ship array
    # and a desired field
    ################################
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

    def getShipField(ship, field):
        field = field.upper()
        return ship[fields[field]]

    # Get a ship's ID
    def getShipId(ship):
        return int(getShipField(ship, "SHIP_ID"))

    # Get a ship's latitude
    def getLatShip(ship):
        return float(getShipField(ship, "LAT"))

    # Get a ship's longtitude
    def getLonShip(ship):
        return float(getShipField(ship, "LON"))

    # Get a ship's heading
    def getHeadingShip(ship):
        return int(getShipField(ship, "HEADING"))

    def getSpeedShip(ship):
        return float(getShipField(ship, "SPEED"))

    def getShipTimeStamp(ship):
        return getShipField(ship, "TIMESTAMP")

    def timeStampCompress(stamp):
        indexT = stamp.find('T')
        return stamp[indexT + 1:]

    def getTimeShip(ship):
        return timeStampCompress(getShipTimeStamp(ship))

    def timeDifferenceSeconds(before, after):
        FMT = '%H:%M:%S'
        return (datetime.strptime(after, FMT) - datetime.strptime(before, FMT)).total_seconds()

    def knotsToMps(knots):
        return knots / 0.51444444444

    def mtoCoor(m):
        return m / 1852