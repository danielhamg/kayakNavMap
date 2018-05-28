import UIKit
import Foundation

// Classes

class Ships {
    var fields = [
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
    ]
    var allShips: [Ships]

    init(_ file: [Ships]) {
        self.allShips
    }

    func predictNextLatLon(ship: Ships, nexTime: Double) -> [Double] {
        let speedX = knotsToMps(cos(getSpeedShip(ship)))
        let speedY = knotsToMps(sin(getSpeedShip(ship)))
        let diffTime = timeDifferenceSeconds(getTimeShip(ship), nexTime)
        let diffX = mtoCoor(speedX * diffTime)
        let diffY = mtoCoor(speedY * diffTime)
        let newLon = getLonShip(ship) + diffX
        let newLat = getLatShip(ship) + diffY
        return [newLon, newLat]
    }

    func getShipField(shipIndex: Int, field: String) -> Double {
        let item = item.upper()
        return self.allShips[index][fields[item]]
    }

    func getShipId(shipIndex: Int) -> Double {
        return self.getShipField(shipIndex: shipIndex, field: "SHIP_ID")
    }

    func getLatShip(shipIndex: Int) -> Double {
        return self.getShipField(shipIndex: shipIndex, field: "LAT")
    }

    func getLonShip(shipIndex: Int) -> Double {
        return self.getShipField(shipIndex: shipIndex, field: "LON")
    }

    func getHeadingShip(shipIndex: Int) -> Double {
        return self.getShipField(shipIndex: shipIndex, field: "HEADING")
    }

    func getSpeedShip(shipIndex: Int) -> Double {
        return getShipField(shipIndex: shipIndex, field: "SPEED")
    }

    func getSpeedTimeStamp(shipIndex: Int) {
        return getShipField(shipIndex: shipIndex, field: "TIMESTAMP")
    }

//    func timeStampCompress(stamp: Int) -> Double {
//        indexT = stamp.find('T')
//        return stamp[indexT + 1:]
//    }
//
//    func getTimeShip(shipIndex: Int) -> Double {
//        return timeStampCompress(getSpeedTimeStamp(shipIndex: ship))
//    }
//
//    func timeDifferenceSeconds(before: Double, after: Double) -> Double {
//        var FMT = '%H:%M:%S'
//        return (datetime.strptime(after, FMT) - datetime.strptime(before, FMT)).total_seconds()
//    }


    func knotsToMps(knots: Double) -> Double {
        return knots / 0.51444444444
    }

    func mtoCoor(m: Double) -> Double {
        return m / 1852
    }
}

class Ahmet {
    var lon: Double
    var lat: Double
    var coordSoFar: [[Double]]
    var coordIndex: Int

    init(_ lon: Double, lat: Double) {
        self.lon = lon
        self.lat = lat
        self.coordSoFar = [[lon, lat]]
        self.coordIndex = 0
    }

    func updateCoord(lon: Double, lat: Double) {
        self.lon = lon
        self.lat = lat
        self.coordSoFar.append([lon, lat])
        self.coordIndex += 1
    }

    func latestCoord() -> [Double] {
        return self.coordSoFar[coordIndex]
    }

    func prevCoord() -> [Double] {
        return self.coordSoFar[coordIndex - 1]
    }
}

// Tests; Main
var x = distanceCalculator(lon1: 10, lat1: 20, lon2: 10, lat2: 21)
print(x)

// .......... Data Processing ..........

func withinRadiusShips(ships: Ships, ahmet: Ahmet) -> [Ships] {
    var withinRadiusShips = [Ships]()
    for i in ships.allShips {
        if booleanWithinRadius(i, ahmet) {
            withinRadiusShips.append(i)
        }
    }
    return withinRadiusShips
}

func withinDirectionShips(withinRadiusShips: [Ships], ahmet: Ahmet) -> [[Ships]] {
    var shipsTowards = [Ships]()
    var shipsAway = [Ships]()
    for i in withinRadiusShips {
        if directionCheck(i, ahmet) {
            shipsTowards.append(i)
        } else {
            shipsAway.append(i)
        }
    }
    return [shipsTowards, shipsAway]
}

// Helper Functions

func booleanWithinRadius(ship: Ships, shipId: Int, ahmet: Ahmet) -> Bool {
    let lonS = ship.getLonShip(shipId)
    let latS = ship.getLatShip(shipId)
    let lonAhmet = Ahmet.getLonShip
    let latAhmet = Ahmet.getLatShip
    if distanceCalculator(lonS, latS, lonAhmet, latAhmet) > 125 {
        return false
    }
    return true
}

func distanceCalculator(lon1: Double, lat1: Double, lon2: Double, lat2: Double) -> Double {
    let R = 6378.137
    let dLon = lon2 * Double.pi / 180 - lon1 * Double.pi / 180
    let dLat = lat2 * Double.pi / 180 - lat1 * Double.pi / 180
    let a = sin(dLat / 2) * sin(dLat / 2)
        + cos(lat1 * Double.pi / 180) * cos(lat2 * Double.pi / 180)
        * sin(dLon/2) * sin(dLon / 2)
    let c = 2 * atan2(sqrt(a), sqrt(1-a))
    let d = R * c
    return d * 1000
}

func directionCheck(ship: Ships, ahmet: Ahmet) -> Bool {
    let oldLat = getLatShip(ship)
    let oldLon = getLonShip(ship)
    let newLat = predictNextLatLon(ship: ship, nexTime: getShipTimeStamp(ship))[0]
    let newLon = predictNextLatLon(ship: ship, nexTime: getShipTimeStamp(ship))[1]
    if distanceCalculator(ahmet.lon, ahmet.lat, newLon, newLat)
        < distanceCalculator(ahmet.lon, ahmet.lat, oldLon, oldLat) {
        return true
    } else {
        return false
    }
}
