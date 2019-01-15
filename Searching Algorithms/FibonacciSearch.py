# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : FibonacciSearch.py
#
# Author            : Ashish Singh
#
# Date created      : 20190115
#
# Purpose           : Implementing Fibonacci Search algorithm in python
#
# **********************************************************************;

class FibonacciSearch:

    def __init__(self):

        # Initialize searching array
        self.searchArray = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]

        # Value to be searched in the array
        self.searchedValue = 50

        # Size of the searching array
        self.arraySize = len(self.searchArray)

    # Returns index of x if present, else returns -1
    def fibonacciSearch(self, searchArray, searchedValue, arraySize):

        # Initialize fibonacci numbers
        fibm2 = 0
        fibm1 = 1
        fibM = fibm2 + fibm1

        # fibM is going to store the smallest Fibonacci Number greater than or equal to n
        while (fibM < arraySize):
            fibm2 = fibm1
            fibm1 = fibM
            fibM = fibm2 + fibm1

        # Marks the eliminated range from front
        offset = -1

        # while there are elements to be inspected.
        # Note that we compare arr[fibMm2] with x and when fibM becomes 1, fibMm2 becomes 0
        while (fibM > 1):

            # Check if fibMm2 is a valid location
            i = min(offset + fibm2, arraySize - 1)

            # If x is greater than the value at index fibMm2, cut the subarray array from offset to i
            if (searchArray[i] < searchedValue):
                fibM = fibm1
                fibm1 = fibm2
                fibm2 = fibM - fibm1
                offset = i

            # If x is greater than the value at index fibMm2, cut the subarray after i+1
            elif (searchArray[i] > searchedValue):
                fibM = fibm2
                fibm1 = fibm1 - fibm2
                fibm2 = fibM - fibm1

            # element found. return index
            else:
                return i

            # comparing the last element with x
        if (fibm1 and searchArray[offset + 1] == searchedValue):
            return offset + 1

        # element not found. return -1
        return -1

    # Function to print index of the element
    def printIndex(self, index):

        # Check for the value of the index, if -1 the value was not found else print the value of index
        if index == -1:
            print("Value was not found in the array")
        else:
            print("Value was found at index : " + str(index))


# Main function that executes when script runs on the console.
if __name__ == "__main__":

    # Create the class object
    fibb = FibonacciSearch()

    # Call Interpolation Search function and print the index
    index = fibb.fibonacciSearch(fibb.searchArray, fibb.searchedValue, fibb.arraySize)

    fibb.printIndex(index)
