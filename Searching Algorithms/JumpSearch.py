# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : JumpSearch.py
#
# Author            : Ashish Singh
#
# Date created      : 20190115
#
# Purpose           : Implementing Jump Search algorithm in python
#
# **********************************************************************;

# Import libraries that are being used
import math

class JumpSearch:

    def __init__(self):

        # Initialize searching array
        self.searchArray = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

        # Value to be searched in the array
        self.searchedValue = 89

        # Size of the searching array
        self.arraySize = len(self.searchArray)


    # Function to print index of the element
    def printIndex(self, index):
        # Check for the value of the index, if -1 the value was not found else print the value of index
        if index == -1:
            print("Value was not found in the array")
        else:
            print("Value was found at index : " + str(index))

    # Function that implements the search algorithm
    def jumpSearch(self, searchArray, searchedValue, arraySize):

        # Finding block size to be jumped
        block = math.sqrt(arraySize)

        # Look for the block in which searched element is present
        leftLimit = 0

        while searchArray[int(min(block, arraySize) - 1)] < searchedValue:
            leftLimit = block
            block += math.sqrt(arraySize)
            if leftLimit >= arraySize:
                return -1

        # Do a linear search in the block found in previous step
        while searchArray[int(leftLimit)] < searchedValue:
            leftLimit += 1

            # If we reach the end of the block and don't find the element return -1 as index
            if leftLimit == min(block, arraySize):
                return -1

        # If element is found in the given block return the value of the index
        if searchArray[int(leftLimit)] == searchedValue:
            return int(leftLimit)

        # If the element is still not found return -1 as index
        return -1


# Main function that executes when script runs on the console.
if __name__ == "__main__":

    jump = JumpSearch()

    index = jump.jumpSearch(jump.searchArray, jump.searchedValue, jump.arraySize)

    jump.printIndex(index)