//
//  Ships.swift
//  MarineTraffic
//
//  Created by Tommy Poa on 24/4/18.
//  Copyright © 2018 Tommy Poa. All rights reserved.
//

import Foundation

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
    
    var allShips: [[String]]
    var inRadius: [[String]]
    var gettingCloser: [[String]]
    var within125: [[String]]
    init(_ file: [[String]]) {
        self.allShips = file
        self.inRadius = []
        self.gettingCloser = []
        self.within125 = []
    }
    
    func predictNextLatLon(ship: [String], nexTime: String) -> [Double] {
        let speedX = knotsToMps(knots: cos(getSpeedShip(ship: ship)))
        let speedY = knotsToMps(knots: sin(getSpeedShip(ship: ship)))
        let diffTime = timeDifferenceSeconds(before: getSpeedTimeStamp(ship: ship), after: nexTime)
        let diffX = mtoCoor(m: speedX * diffTime)
        let diffY = mtoCoor(m: speedY * diffTime)
        let newLon = getLonShip(ship: ship) + diffX
        let newLat = getLatShip(ship: ship) + diffY
        return [newLon, newLat]
    }
    
    func getShipField(ship: [String], field: String) -> String {
        let field = field.uppercased()
        return ship[fields[field]!]
    }
    
    func getShipId(ship: [String]) -> Int32 {
        return Int32(self.getShipField(ship: ship, field: "SHIP_ID"))!
    }
    
    func getLatShip(ship: [String]) -> Double {
        return Double(self.getShipField(ship: ship, field: "LAT"))!
    }
    
    func getLonShip(ship: [String]) -> Double {
        return Double(self.getShipField(ship: ship, field: "LON"))!
    }
    
    func getHeadingShip(ship: [String]) -> Double {
        return Double(self.getShipField(ship: ship, field: "HEADING"))!
    }
    
    func getSpeedShip(ship: [String]) -> Double {
        return Double(getShipField(ship: ship, field: "SPEED"))!
    }
    
    func getSpeedTimeStamp(ship: [String]) -> String {
        return getShipField(ship: ship, field: "TIMESTAMP")
    }

    func timeDifferenceSeconds(before: String, after: String) -> Double {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "yyyy-MM-dd'T'HH:mm:ss"
        let beforeDate = dateFormatter.date(from: before)!
        let afterDate = dateFormatter.date(from: after)!
        return afterDate.timeIntervalSince(beforeDate)
    }

    func knotsToMps(knots: Double) -> Double {
        return knots / 0.51444444444
    }
    
    func mtoCoor(m: Double) -> Double {
        return m / 1852
    }
}
