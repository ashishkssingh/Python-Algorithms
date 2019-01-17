# **********************************************************************;
# Project           : Learning Algorithms
# 
# Program name      : LinearSearch.py
#
# Author            : Ashish Singh
#
# Date created      : 20181220
#
# Purpose           : Implementing Linear Search Algorithm in python
#
# **********************************************************************;

class LinearSearch:

    def __init__(self):

        self.searchArray = [54, 89, 43, 36, 34, 100, 56, 39, 12, 31]

        self.searchedValue = 100

        self.arraySize = len(self.searchArray)

    def printIndex(self, index):

        # Check for the value of the index
        if index == -1:
            print("Value was not found in the array")
        else:
            print("Value was found at index : " + str(index))

    # Function that implements Linear Search algorithm
    def linearSearch(self):

        searchArray = self.searchArray

        searchedValue = self.searchedValue

        # Loop through all the elements in the array for searched value
        for i in range(len(searchArray)):

            # If searched value is found at an index return the index
            if searchArray[i] == searchedValue:
                return i
        # If the searched value is not present in the array return -1 as the index
        return -1


# Main function that executes when script runs on the console.
if __name__ == "__main__":

    linear = LinearSearch()

    index = linear.linearSearch()

    linear.printIndex(index)
