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

# Import libraries that are being used
import math

# Function that implements the search algorithm
def jumpSearch(searchArray, searchedValue, arraySize):

    # Finding block size to be jumped
    block = math.sqrt(arraySize)

    # Look for the block in which searched element is present
    prev = 0
    while searchArray[int(min(block, arraySize) - 1)] < searchedValue:
        prev = block
        block += math.sqrt(arraySize)
        if prev >= arraySize:
            return -1

    # Do a linear search in the block found in previous step
    while searchArray[int(prev)] < searchedValue:
        prev += 1

        # If we reach the end of the block and don't find the element return -1 as index
        if prev == min(block, arraySize):
            return -1

    # If element is found in the given block return the value of the index
    if searchArray[int(prev)] == searchedValue:
        return int(prev)
    
    # If the element is still not found return -1 as index     
    return -1

# Function to print index of the element
def printIndex(index):
    
    # Check for the value of the index, if -1 the value was not found else print the value of index
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
