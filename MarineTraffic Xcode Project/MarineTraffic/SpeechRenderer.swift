//
//  SpeechRenderer.swift
//  MarineTraffic
//
//  Created by Tommy Poa on 29/4/18.
//  Copyright © 2018 Tommy Poa. All rights reserved.
//

import Foundation
import UIKit

class SpeechRenderer {
    
    static var directionFields = [
        1 : "1 o clock direction",
        2 : "2 o clock direction",
        3 : "3 o clock direction",
        4 : "4 o clock direction",
        5 : "5 o clock direction",
        6 : "6 o clock direction",
        7 : "7 o clock direction",
        8 : "8 o clock direction",
        9 : "9 o clock direction",
        10 : "10 o clock direction",
        11 : "11 o clock direction",
        12 : "12 o clock direction"
    ]
    
    
    static func renderSpeech(twoAShips: [[String]], ahmetLon: Double, ahmetLat: Double) -> [String] {
        var result = [String]()
        if twoAShips.isEmpty {
            result.append("There are no ships near you currently.")
        } else {
            for ship in twoAShips {
                var helperString = "There is a ship in your"
                let shipLat = Double(ship[3])
                let shipLon = Double(ship[4])
                let bearing = pointPairToBearingDegrees(startingPoint: CGPoint(x: ahmetLat, y: ahmetLon), endingPoint: CGPoint(x: shipLat!, y: shipLon!))
                let directionNumber = getDirectionNumber(bearing: bearing)
                helperString.append(directionFields[directionNumber]!)
                
                helperString.append(", and it is")
                let distance = Int(DataProcessing.distanceCalculator(lon1: ahmetLon, lat1: ahmetLat, lon2: shipLon!, lat2: shipLat!))
                let distanceString = "\(distance)"
                helperString.append(distanceString + "meters away.")
                
                result.append(helperString)
            }
        }
        return result
    }
    
    static func pointPairToBearingDegrees(startingPoint: CGPoint, endingPoint: CGPoint) -> Double {
        let originPoint = CGPoint(x: (endingPoint.x - startingPoint.x), y: (endingPoint.y - startingPoint.y)); // getorigin point to origin by subtracting end from start
        let bearingRadians = atan2f(Float(originPoint.y), Float(originPoint.x)); // get bearing in radians
        var bearingDegrees = Double(bearingRadians) * (180.0 / Double.pi); // convert to degrees
        bearingDegrees = (bearingDegrees > 0.0 ? bearingDegrees : (360.0 + bearingDegrees)); // correct discontinuity
        return bearingDegrees;
    }
    
    static func getDirectionNumber(bearing: Double) -> Int {
        if (15 <= bearing && bearing < 45) {
            return 2
        } else if (45 < bearing && bearing < 75) {
            return 1
        } else if (75 < bearing && bearing < 105) {
            return 12
        } else if (105 < bearing && bearing < 135) {
            return 11
        } else if (135 < bearing && bearing < 165) {
            return 10
        } else if (165 < bearing && bearing < 195) {
            return 9
        } else if (195 < bearing && bearing < 225) {
            return 8
        } else if (225 < bearing && bearing < 255) {
            return 7
        } else if (255 < bearing && bearing < 285) {
            return 6
        } else if (285 < bearing && bearing < 315) {
            return 5
        } else if (315 < bearing && bearing < 345) {
            return 4
        } else {
            return 3
        }
    }
}
