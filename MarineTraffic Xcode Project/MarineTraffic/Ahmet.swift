//
//  Ahmet.swift
//  MarineTraffic
//
//  Created by Tommy Poa on 24/4/18.
//  Copyright © 2018 Tommy Poa. All rights reserved.
//

import Foundation

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
