# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : BinarySearch.py
#
# Author            : Ashish Singh
#
# Date created      : 20181221
#
# Purpose           : Implementing Binary Search Algorithm in python
#
# **********************************************************************;

class BinarySearch:

    searchArray = []
    searchedValue = 0
    arraySize = 0

    def __init__(self):

        self.searchArray = [54, 89, 43, 36, 34, 100, 56, 39, 12, 31]

        self.searchedValue = 56

        self.arraySize = len(self.searchArray)


    def printIndex(self, index):

        # Check for the value of the index
        if index == -1:
            print("Value was not found in the array")
        else:
            print("Value was found at index : " + str(index))

    # Function that uses binary search
    def binarySearch(self, leftLimit, rightLimit):

        searchedValue = self.searchedValue

        searchArray = self.searchArray

        # Check base case
        if rightLimit >= leftLimit:

            middleElement = leftLimit + (rightLimit - leftLimit) / 2

            # If element is present at the middle itself
            if searchArray[middleElement] == searchedValue:
                return middleElement

            # If element is smaller than mid, then it
            # can only be present in left subarray
            elif searchArray[middleElement] > searchedValue:
                return self.binarySearch(leftLimit, middleElement - 1)

            # Else the element can only be present
            # in right subarray
            else:
                return self.binarySearch(middleElement + 1, rightLimit)

        else:
            # Element is not present in the array
            return -1


# Main function that executes when script runs on the console.
if __name__ == "__main__":

    binary = BinarySearch()

    index = binary.binarySearch(0, binary.arraySize - 1)

    binary.printArray(index)