# **********************************************************************;
# Project           : Learning Algorithms
# 
# Program name      : insertionSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190110
#
# Purpose           : Implementing insertion sort algorithm in python
#
# **********************************************************************;

# Function that implements insertion sort
def insertionSort(unsortedArray, arrayLength, sortingType):

    for i in range(1, arrayLength):

        # Select the first element if the loop as key
        key = unsortedArray[i]

        j = i - 1

        if sortingType == "Ascending" or sortingType == "Asc" or sortingType == "ascending" or sortingType == "asc":
            while j >= 0 and key < unsortedArray[j]:
                unsortedArray[j + 1] = unsortedArray[j]
                j -= 1

        else:
            while j >= 0 and key > unsortedArray[j]:
                unsortedArray[j + 1] = unsortedArray[j]
                j -= 1

        unsortedArray[j + 1] = key

    # Call printArray function to print the sorted array
    printSortedArray(unsortedArray)


# Function to print Sorted Array
def printSortedArray(sortedArray):
    string = ""

    for i in range(len(sortedArray)):
        string += str(sortedArray[i]) + " "

    # Print Sorted array to the console
    print(string)


# Main function that executes when script runs on the console.
if __name__ == "__main__":

    # Test values for sorting
    unsortedArray = [18, 75, 77, 70, 32, 15, 71, 64, 67, 14]

    # get length of the array
    arrayLength = len(unsortedArray)

    # Select sorting type
    sortingType = "Desc"

    # Calling insertion sort function
    insertionSort(unsortedArray, arrayLength, sortingType)
