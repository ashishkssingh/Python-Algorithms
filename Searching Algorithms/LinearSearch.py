# **********************************************************************;
# Project           : Learning Algorithms
# 
# Program name      : LinearSearch.py
#
# Author            : Ashish Singh
#
# Date created      : 20181215
#
# Purpose           : Implementing Linear Search Algorithm in python
#
# **********************************************************************;

def LinearSearch(searchArray, searchedValue):

    # Loop through all the elements in the array for searched value
    for i in range(len(searchArray)):

        # If searched value is found at an index return the index
        if searchArray[i] == searchedValue:
            return i
    # If the searched value is not present in the array return -1 as the index
    return -1


def printIndex(index):
    # Check for the value of the index
    if index == -1:
        print("Value was not found in the array")
    else:
        print("Value was found at index : " + str(index))


if __name__ == "__main__":
    # Initialize searching array
    searchArray = [2, 3, 4, 10, 40]

    # Value to be searched in the array
    searchedValue = 4

    # Call Linear Search function and print the index
    printIndex(LinearSearch(searchArray, searchedValue))
