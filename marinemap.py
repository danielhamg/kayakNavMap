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
def withinRadiusShips(listOfShips):
#returns ships that are within a radius of 125m

	def helper(i):

		return false

	withinRadiusShips = []
	for i in listOfShips:
		if helper(i):
			withinRadiusShips.append(i)
	
	return withinRadiusShips




def degToMeters(degreeData)
#converting lat and long from degrees to metric scale

def distanceCalculator(latShip, latAhmet, longShip, longAhmet)
#returns the distance between ship and Ahmet
	return sqrt(((latShip - latAhmet) ** 2) + ((longShip - longAhmet) ** 2))


### 2B: Direction Filter: Identifying ships from 2A that is moving towards Ahmet
def withinDirectionShips(withinRadiusShips)
#returns ships that are in radius and towards Ahmet

	return finalShips



def shipMoving
#returns whether ship is moving
	return speed not nil