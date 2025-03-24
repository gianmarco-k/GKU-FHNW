#Aufgabe 1

import math

class Vector3:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
v = Vector3(2, 2, 2)
print(f"Die Länge des Vectors ist: {v.len()}")


#Aufgabe 2

class WGS84Coord:
    def __init__(self, lo = 0, la = 0):
        self._longitude = lo
        self._latitude = la
    
    def setlongitude(self, lo):
        if lo < -180:
            raise ValueError("Longitude darf nicht kleiner als -180 sein!")
        elif lo > 180:
            raise ValueError("Longitude darf nicht grösser als 180 sein!")
        self._longitude = lo
    
    def getlongitude(self):
        return self._longitude
    
    def setlatitude(self, la):
        if la < -90:
            raise ValueError("Latitude darf nicht kleiner als -90 sein!")
        elif la > 90:
            raise ValueError("Latitude darf nicht grösser als 90 sein!")
        self._latitude = la
    
    def getlatitude(self):
        return self._latitude
    
    longitude = property(getlongitude, setlongitude)
    latitude = property(getlatitude, setlatitude)
    
        
coord = WGS84Coord(200, -100)
print(f"Koordinaten: Longitude = {coord.longitude} Latitude = {coord.latitude}")