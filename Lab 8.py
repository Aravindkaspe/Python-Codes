# Aravind Kumar Kaspe
# Banner ID : 001291145

# Lab - 8

from math import *

class vector3f:

    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y

    def setZ(self, z):
        self._z = z

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getZ(self):
        return self._z

    def addVectors(self, vector):
        return vector3f(vector.getX() + self.getX(),
                        vector.getY() + self.getY(),  
                        vector.getZ() + self.getZ())

    def scaleVector(self, scale):
        self._x = self._x * scale
        self._y = self._y * scale
        self._z = self._z * scale

    def lengthofVector(self):
        return sqrt(self._x**2 + self._y**2 + self._z**2)

    def dotProduct(self, vector):
        product = vector.getX() * self.getX() + vector.getY() * self.getY() + vector.getZ() * self.getZ()
        return product

class vector4f(vector3f):
    
    def __init__(self, _x, _y, _z, w):
        super().__init__(_x, _y, _z)
        self._w = w

    def setW(self, w):
        self._w = w

    def getW(self):
        return self._w

    def __add__(self, vector):
        vector3dSum = super().addVectors(vector)
        return vector4f(vector3dSum.getX(), vector3dSum.getY(), vector3dSum.getZ(), 
                        self._w + vector.getW())

    def __mul__(self, multiplier):
        if isinstance(multiplier, vector3f):
            vector3dMul = super().dotProduct(multiplier)
            return vector3dMul + (self._w * multiplier.getW())
        else:
            super().scaleVector(multiplier)
            self.setW(multiplier * self._w)

    def findLengthOfVector(self):
        return (self._x**2 + self._y**2 + self._z**2 + self._w**2)**(1/2)

    def normalizeVector(self):
        vectorLength = self.findLengthOfVector()
        if vectorLength > 0:
            self.setX(self._x / vectorLength)
            self.setY(self._y / vectorLength)
            self.setZ(self._z / vectorLength)
            self.setW(self._w / vectorLength)
    
    def __str__(self):
        return f' {self.getX()} , {self.getY()} , {self.getZ()} , {self.getW()}'

vector_one = vector4f(3, 1, 4, 2)
vector_two = vector4f(5, 7, 6, 9)

print("vector one:", vector_one)
print("vector two:", vector_two)
print()

vector_one_len = vector_one.findLengthOfVector()
vector_two_len = vector_two.findLengthOfVector()

print("vector one magnitude:", vector_one_len)
print("vector two magnitude:", vector_two_len)  
print()

vectorDotProduct = vector_one * vector_two
print("The dot product of two vectors:", vectorDotProduct)
print()

vector_one_ScalarMul = vector_one * 3
vector_two_ScalarMul = vector_two * 3
print("vector one multiplied by 3:", vector_one)
print("vector two multiplied by 3:", vector_two)
print()   

vectorSum = vector_one + vector_two
print("vector sum:", vectorSum)
vectorSum.normalizeVector()
print("normalized vector sum:",vectorSum)
