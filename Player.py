#
#
# Aravind Kumar Kaspe
# Banner ID: 001291145
#
# Description : This program defines a class named "Player" with two instance
#               variables, _number (an integer) and _name (a string representing
#               the player's full name). This class, features a constructor
#               that initializes these variables based on provided parameters.
#               Four public instance methods provide access and modification
#               of player information: getNumber() and getName() retrieve the
#               player's number and name, respectively, while setNumber(number)
#               and setName(name) allow for updating these attributes.
#
#
class Player:
    # Player Class Definition
    #
    # 2 Instance Variables:
    # _number int
    # _name str - first & last name together in 1 str
    #
    # Constructor:
    # __init__(self, number, name) Initialize _number to number,
    # _name to name    
    #
    # 4 Public Instance Methods: 
    # getNumber(self) return _number
    # getName(self) return _name
    # setNumber(self, number) set _number to number
    # setName(self, name) set _name to name
    #
    #
    def __init__(self, number, name):
        self._number = number
        self._name = name

    def getNumber(self):
        return self._number

    def getName(self):
        return self._name

    def setNumber(self, number):
        self._number = number

    def setName(self, name):
        self._name = name
