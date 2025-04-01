# Aufgabe 1

import math

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Vector3 (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
    
    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Addition ist nur mit einem anderen Vector3 möglich.")
    
    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError("Subtraktion ist nur mit einem anderen Vector3 möglich.")
    
    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (float, int)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        raise TypeError("Multiplikation ist nur mit einem Skalar oder einem Vector3 möglich.")
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def dot(self, other):
        if isinstance(other, Vector3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise TypeError("Skalarprodukt ist nur mit einem anderen Vector3 möglich.")
    
    def cross(self, other):
        if isinstance(other, Vector3):
            return Vector3(
                self.y * other.z - self.z * other.y,
                self.z * other.x - self.x * other.z,
                self.x * other.y - self.y * other.x
            )
        raise TypeError("Kreuzprodukt ist nur mit einem anderen Vector3 möglich.")
    
    def normalize(self):
        length = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        if length == 0:
            raise ValueError("Ein Null-Vektor kann nicht normalisiert werden.")
        return Vector3(self.x / length, self.y / length, self.z / length)


a = Vector3(3,4,2)
print(a)
b = Vector3(2,1,0)
print(b)

c = a * b
print(c)

d = a.dot(b)
print(d)
e = a.cross(b)
print(e)



