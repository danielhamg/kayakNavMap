### 1: Getting relevant data ###
# from math import *
# from datetime import datetime *
from math import *
from datetime import datetime
import time

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

# ship is a list
def getShipField(ship, item):
        item = item.upper()
        return ship[fields[item]]

def getLatShip(ship):
    return float(getShipField(ship, "lat"))

# get a ship's longtitude
def getLonShip(ship):
    return float(getShipField(ship, "lon"))

# get a ship's heading
def getHeadingShip(ship):
    return float(getShipField(ship, "heading"))

def getSpeedShip(ship):
    return float(getShipField(ship, "speed"))

def getSpeedTimeStamp(ship):
    return getShipField(ship, "timestamp")


def timeStampCompress(stamp):
    indexT = stamp.find('T')
    return stamp[indexT + 1:]

def timeDifferenceSeconds(before, after):
    FMT = '%H:%M:%S'
    return (datetime.strptime(after, FMT) - datetime.strptime(before, FMT)).total_seconds()
    
def knotsToMps(knots):
    return knots / 0.51444444444

def mtoCoor(m):
    return m / 1852

def getTimeShip(ship):
#     print(timeStampCompress(getSpeedTimeStamp(ship)))
    return timeStampCompress(getSpeedTimeStamp(ship))


# latitude, longitude
# up is increase in lat
# right is increase in long
def predictNextLatLon(ship, nexTime):
    speedX = knotsToMps(cos(getSpeedShip(ship)))
    speedY = knotsToMps(sin(getSpeedShip(ship)))
#     print(getTimeShip(ship), " ", nexTime)
    diffTime = timeDifferenceSeconds(getTimeShip(ship), nexTime)
    diffX = mtoCoor(speedX * diffTime)    # should be in coor
    diffY = mtoCoor(speedY * diffTime)    # should be in coor
    newLon = getLonShip(ship) + diffX
    newLat = getLatShip(ship) + diffY
    return [newLat, newLon] # in latitude, then longitude



### 1A: Querying MarineTraffic data ###
def queryData():

	#returns all relevant information that is needed for parts B
	#accounts for timestamp offset
	return listOfShips

def toCartesian(num):
	# convert something in the heading sphere (top is 0 deg) into normal coor plane
	if (0 <= num and num < 90):
		return 90 - num
	elif (90 <= num and num < 180):
		return 270 + 180 - num
	elif (180 <= num and num < 270):
		return 180 + 270 - num
	elif (270 <= num and num <= 360):
		return 90 + 360 - num

def headingQuadrant(num):
	if (0 <= num and num < 90):
		return 1
	elif (90 <= num and num < 180):
		return 4
	elif (180 <= num and num < 270):
		return 3
	elif (270 <= num and num <= 360):
		return 2



def getPredictedLon(ship, nexTime):
	# accounting for ship offset time based on timestamps. Gets predicted latitude based on last timestamp and also curent
	quadrant = headingQuadrant(getHeadingShip(ship))
	if (quadrant == 1):
		xspeed = getSpeedShip(ship) * math.cos(x)
		yspeed = getSpeedShip(ship) * math.sin(x)

		return None
	if (quadrant == 2):
		return None
	if (quadrant == 3):
		return None
	if (quadrant == 4):
		return None
		



def getPredictedLat(ship, nexTime):
	return None




### 1B: Getting Ahmet's GPS location ###
# def queryAhmetData()


### 2: Filtering necessary ship information for Ahmet ###

### 2A: Radius Filter: Identifying ships within given radius ###
def withinRadiusShips(listOfShips, Ahmet):
#returns ships that are within a radius of 125m
	withinRadiusShips = []
	for i in listOfShips:
		if booleanWithinRadius(i, Ahmet):
			withinRadiusShips.append(i)
	return withinRadiusShips

def booleanWithinRadius(ship, Ahmet):
	latS = ship.getLatShip
	longS = ship.getLonShip
	latAhmet = Ahmet.getLatShip
	longAhmet = Ahmet.getLonShip
	if (distance(latS, longS, latAhmet, longAhmet) > 125):
		return false
	return true

# def distanceCalculator(lat1, lon1, lat2, lon2):
# 	# Source: https://stackoverflow.com/questions/639695/how-to-convert-latitude-or-longitude-to-meters
# 	#returns the distance between ship and Ahmet
#     # R = 6378.137;
#     # dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180;
#     # dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180;
#     # a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
#     # math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * \
#     # math.sin(dLon/2) * math.sin(dLon / 2);
#     # c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
#     # d = R * c;
#     # return d * 1000;

# def distanceCalculator(latShip, latAhmet, longShip, longAhmet):
# 	return sqrt(((latShip - latAhmet) ** 2) + ((longShip - longAhmet) ** 2))

# def degToMeters(degreeData)
# #converting lat and long from degrees to metric scale


### 2B: Direction Filter: Identifying ships from 2A that is moving towards Ahmet
def withinDirectionShips(withinRadiusShips, Ahmet):
#returns ships that are in radius and towards Ahmet
	# return finalShips
	return None

def testFunction():
	return None