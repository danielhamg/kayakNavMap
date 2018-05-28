//
//  DataProcessing.swift
//  MarineTraffic
//
//  Created by Tommy Poa on 24/4/18.
//  Copyright © 2018 Tommy Poa. All rights reserved.
//

import Foundation

class DataProcessing {
    
    static func withinRadiusShips(ships: Ships, ahmet: Ahmet) -> [[String]] {
        var withinRadiusShips = [[String]]()
        for i in ships.allShips {
            if booleanWithinRadius(ships: ships, ship: i, ahmet: ahmet) {
                withinRadiusShips.append(i)
            }
        }
        return withinRadiusShips
    }
    
    // Helper Functions
    
    static func booleanWithinRadius(ships: Ships, ship: [String], ahmet: Ahmet) -> Bool {
        let lonS = ships.getLonShip(ship: ship)
        let latS = ships.getLatShip(ship: ship)
        let lonAhmet = ahmet.lon
        let latAhmet = ahmet.lat
        if distanceCalculator(lon1: lonS, lat1: latS, lon2: lonAhmet, lat2: latAhmet) > 500 {
            return false
        }
        return true
    }
    
    static func distanceCalculator(lon1: Double, lat1: Double, lon2: Double, lat2: Double) -> Double {
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

    
    
}
