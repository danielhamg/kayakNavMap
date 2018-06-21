func withinRadiusShips(ships: Ships, ahmet: Ahmet) -> Array {
  var withinRadiusShips = [Ships]()
  for i in ships.allShips {
    if booleanWithinRadius(i, ahmet) {
      withinRadiusShips.append(i)
    }
  }
  return withinRadiusShips
}

func withinDirectionShips(withinRadiusShips: Array, ahmet: Ahmet) {
  var shipsTowards = [Ships]()
  var shipsAway = [Ships]()
  for i in withinRadiusShips {
    if directionCheck(i, ahmet) {
      shipsTowards.append(i)
    } else {
      shipsAway.append(i)
    }
  }
  return (shipsTowards, shipsAway)
}

//######################################################//
//################## HELPER FUNCTIONS ##################//
//######################################################//

func booleanWithinRadius(ship, ahmet) {
  lonS = ship.getLonShip
  latS = ship.getLatShip
  lonAhmet = Ahmet.getLonShip
  latAhmet = Ahmet.getLatShip
  if distanceCalculator(lonS, latS, lonAhmet, latAhmet) > 125 {
    return false
  }
    return true
}

func distanceCalculator(lon1, lat1, lon2, lat2) {
  var R = 6378.137
  var dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180
  var dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
  var a = math.sin(dLat / 2) * math.sin(dLat / 2)
  + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180)
  * math.sin(dLon/2) * math.sin(dLon / 2)
  var c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  var d = R * c
  return d * 1000
}
