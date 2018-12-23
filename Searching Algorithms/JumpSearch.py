# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : JumpSearch.py
#
# Author            : Ashish Singh
#
# Date created      : 20181222
#
# Purpose           : Implementing Jump Search algorithm in python
#
# **********************************************************************;

# Import libraries used
import math

# Function that implements the search algorithm
def jumpSearch(searchArray, searchedValue, arraySize):

    # Finding block size to be jumped
    step = math.sqrt(arraySize)

    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while searchArray[int(min(step, arraySize) - 1)] < searchedValue:
        prev = step
        step += math.sqrt(arraySize)
        if prev >= arraySize:
            return -1

    # Doing a linear search for searchedValue in
    # block beginning with prev.
    while searchArray[int(prev)] < searchedValue:
        prev += 1

        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, arraySize):
            return -1

    # If element is found
    if searchArray[int(prev)] == searchedValue:
        return int(prev)

    return -1

# Function to print index of the element
def printIndex(index):
    
    # Check for the value of the index
    if index == -1:
        print("Value was not found in the array")
    else:
        print("Value was found at index : " + str(index))

# Main function that executes when script runs on the console.
if __name__ == "__main__":
    
    # Initialize searching array
    searchArray = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

    # Value to be searched in the array
    searchedValue = 55

    # Size of the searching array
    arraySize = len(searchArray)

    # Call Linear Search function and print the index
    printIndex(jumpSearch(searchArray, searchedValue, arraySize))
