# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : InterpolationSearch.py
#
# Author            : Ashish Singh
#
# Date created      : 20181227
#
# Purpose           : Implementing Interpolation Search algorithm in python
#
# **********************************************************************;

# Function that implements the search algorithm
def interpolationSearch(searchArray, arraySize, searchedValue):

    # Set lower and upper limit of search index
    low = 0
    high = (arraySize - 1)

    # Since array is sorted, an element present
    # in array must be in range defined by corner
    while low <= high and searchArray[low] <= searchedValue <= searchArray[high]:
        # Probing the position with keeping
        # uniform distribution in mind.
        position = low + int(((float(high - low)/(searchArray[high] - searchArray[low])) * (searchedValue - searchArray[low])))

        # Condition of target found
        if searchArray[position] == searchedValue:
            return position

        # If x is larger, x is in upper part
        if searchArray[position] < searchedValue:
            low = position + 1;

        # If x is smaller, x is in lower part
        else:
            high = position - 1;

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
    printIndex(interpolationSearch(searchArray, searchedValue, arraySize))
