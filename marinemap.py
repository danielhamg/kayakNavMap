### 1: Getting relevant data ###

### 1A: Querying MarineTraffic data ###
def queryData()
#returns all relevant information that is needed for parts B
#accounts for timestamp offset
return listOfShips

def timeOffset()
# accounting for ship offset time based on timestamps


### 1B: Getting Ahmet's GPS location ###
def queryAhmetData


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

def distanceCalculator(lat1, lon1, lat2, lon2):
	# Source: https://stackoverflow.com/questions/639695/how-to-convert-latitude-or-longitude-to-meters
	#returns the distance between ship and Ahmet
    R = 6378.137;
    dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180;
    dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180;
    a = math.sin(dLat / 2) * math.sin(dLat / 2) +
    math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) *
    math.sin(dLon/2) * math.sin(dLon / 2);
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
    d = R * c;
    return d * 1000;

# def distanceCalculator(latShip, latAhmet, longShip, longAhmet):
# 	return sqrt(((latShip - latAhmet) ** 2) + ((longShip - longAhmet) ** 2))

# def degToMeters(degreeData)
# #converting lat and long from degrees to metric scale


### 2B: Direction Filter: Identifying ships from 2A that is moving towards Ahmet
def withinDirectionShips(withinRadiusShips, Ahmet)
#returns ships that are in radius and towards Ahmet
	return finalShips