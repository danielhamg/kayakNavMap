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

    # Constructor: takes in JSON file / array(?)
    def __init__(self, file):
        self.allShips = file
        self.inRadius = []
        self.gettingCLoser = []
        self.within125 = []


    ######################################################
    ################## HELPER FUNCTIONS ##################
    ######################################################
    def getAllShips(self):
        return self.allShips
    
    # returns a ship with a particular id in this timestep of ships
    def getShipWithId(self, idnum):
        for ship in self.getAllShips():
            if self.getShipId(ship) == idnum:
                return ship
        return None

        

    # Gets the output of a particular ship's field; General helper function
#     def getShipField(self, shipIndex, field):
#         field = field.upper()
#         return self.allShips[index][Ships.fields[field]]
    
    def getShipField(self, ship, field):
        field = field.upper()
        return ship[Ships.fields[field]]

    # Get a ship's ID
    # def getShipId(self, shipIndex):
        # return int(self.getShipField(shipIndex, "SHIP_ID"))
    def getShipId(self, ship):
            return int(self.getOneShipField(ship, "SHIP_ID"))

    # Get a ship's latitude
    def getLatShip(self, ship):
        return int(self.getShipField(ship, "LAT"))

    # Get a ship's longtitude
    def getLonShip(self, ship):
        return int(self.getShipField(ship, "LON"))

    # Get a ship's heading
    def getHeadingShip(self, ship):
        return int(self.getShipField(ship, "HEADING"))

    def getSpeedShip(self, ship):
        return float(getShipField(ship, "SPEED"))

    def getTimeStamp(self, ship):
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
