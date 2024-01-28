#
# Aravind Kumar Kaspe
# Banner ID : 001291145
#
# Lab - 7
#
#
from math import *

class vector3f:
    def __init__(self,x=0,y=0,z=0):
        self._x = x
        self._y = y
        self._z = z

    def setX(self,x):
        self._x = x

    def setY(self,y):
        self._y = y

    def setZ(self,z):
        self._z = z

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getZ(self):
        return self._z

    def addVectors(vector1,vector2):
        return vector3f(vector1.getX() + vector2.getX() , vector1.getY() + vector2.getY() , vector1.getZ() + vector2.getZ())

    def scaleVector(self,scale):
        self._x = self._x * scale
        self._y = self._y * scale
        self._z = self._z * scale

    def lengthofVector(self):
        return sqrt( self._x**2 + self._y**2 + self._z**2)

    def dotProduct(vector1,vector2):
        product=vector1.getX() * vector2.getX() + vector1.getY()* vector2.getY() + vector1.getZ() * vector2.getZ()
        return product


vector1 = vector3f(3, 1, 2)
vector2 = vector3f(4, 5, 6)

print(f'vector one: {vector1.getX()} , {vector1.getY()} , {vector1.getZ()}')
print(f'vector two: {vector2.getX()} , {vector2.getY()} , {vector2.getZ()}')
print()
print("vector one magnitude:", vector1.lengthofVector())
print("vector two magnitude:", vector2.lengthofVector())
print()
print("The dot product of the two vectors:", vector1.dotProduct(vector2),end='\n\n')

vector1.scaleVector(3)
vector2.scaleVector(3)

print(f'vector one multiplied by 3: {vector1.getX()} , {vector1.getY()} , {vector1.getZ()}')
print(f'vector two multiplied by 3: {vector2.getX()} , {vector2.getY()} , {vector2.getZ()}')
vector3 = vector1.addVectors(vector2)
print(f'\nvector sum: {vector3.getX()} , {vector3.getY()} , {vector3.getZ()}')
