#
# Aravind Kumar kaspe
# Banner ID: 001291145
#
# Description: This class is a subclass of Python's built-in list class.
#              It does not introduce any additional instance variables.
#              The init constructor simply calls the parent class constructor.
#              The class has one public instance method called "find," which
#              performs a sequential search of the list starting from location
#              0 until the target element is found or the end of the list is
#              reached. The method returns a list with two values: the first
#              value is True if the element was found and False otherwise, and
#              the second value is the number of locations visited during
#              the search.
#
#

class UnsortedList(list):
    #
    # class UnsortedList is a subclass of Python's built-in list class
    #
    # No additional Instance Variables
    #
    # Constructor:
    #           __init__(self) Simply calls the parent function constructor
    #
    # 1 Public Instance Method:
    # find(self, element)  Executes a sequential search of the list
    #                      starting at location 0 and continuing until
    #                      element is found or the end of the list is
    #                      reached. Returns a list with 2 values - the
    #                      first value is True if element was found,
    #                      False otherwise - the second value is the
    #                      number of locations visited during the search.
    #
    def __int__(self):
        super().__init__()

    def find(self, element):

        size = len(self)
        found = False
        for index in range(size):
            if self[index] == element:
                found = True
        return [found,index+1]

