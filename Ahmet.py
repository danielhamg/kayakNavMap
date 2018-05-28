class Ahmet:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat
        self.coordSoFar = [(lon, lat)]
        self.coordIndex = 0

    def updateCoord(lon, lat):
        self.lon = lon
        self.lat = lat
        self.coordSoFar.append((lon, lat))
        self.coordIndex += 1

    def latestCoord():
        return self.coordSoFar[coordIndex]

    def prevCoord():
        return self.coordSoFar[coordIndex - 1]
