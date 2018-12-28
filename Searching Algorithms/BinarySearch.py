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

# Function that uses binary search
def BinarySearch(searchArray, leftLimit, rightLimit, searchedValue):

    # Check base case
    if rightLimit >= leftLimit:

        middleElement = leftLimit + (rightLimit - leftLimit) / 2

        # If element is present at the middle itself
        if searchArray[middleElement] == searchedValue:
            return middleElement

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif searchArray[middleElement] > searchedValue:
            return BinarySearch(searchArray, leftLimit, middleElement - 1, searchedValue)

        # Else the element can only be present
        # in right subarray
        else:
            return BinarySearch(searchArray, middleElement + 1, rightLimit, searchedValue)

    else:
        # Element is not present in the array
        return -1

# Function that prints the index of the element
def printIndex(index):
    
    # Check for the value of the index
    if index == -1:
        print("Value was not found in the array")
    else:
        print("Value was found at index : " + str(index))


# Main function that executes when script runs on the console.
if __name__ == "__main__":
    # Initialize searching array
    searchArray = [2, 3, 4, 10, 40]

    # Length of Search Array
    arrayLength = len(searchArray)

    # Value to be searched in the array
    searchedValue = 10

    # Call Binary Search function and print the index
    printIndex(BinarySearch(searchArray, 0, arrayLength, searchedValue))
