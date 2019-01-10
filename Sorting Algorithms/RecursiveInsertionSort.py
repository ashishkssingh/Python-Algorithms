# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : RecursiveInsertionSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190110
#
# Purpose           : Implementing recursive insertion sort algorithm in python
#
# **********************************************************************;

# Function that implements recursive insertion sort
def RecursiveInsertionSort(unsortedArray, arrayLength, sortingType):

    # Base case to exit out of the recursion loop
    if arrayLength <= 1:
        return

    # Sort first n-1 elements
    RecursiveInsertionSort(unsortedArray, arrayLength - 1, sortingType)

    # Insert the last element in the correct position and use it as key   
    last = unsortedArray[arrayLength - 1]
    j = arrayLength - 2

    if sortingType == "Ascending" or sortingType == "ascending" or sortingType == "Asc" or sortingType == "asc":
        # Move all the values greater than the key one position ahead.
        while j >= 0 and unsortedArray[j] > last:
            unsortedArray[j + 1] = unsortedArray[j]
            j = j - 1

    else:
        # Move all the values greater than the key one position ahead.
        while j >= 0 and unsortedArray[j] < last:
            unsortedArray[j + 1] = unsortedArray[j]
            j = j - 1

    unsortedArray[j + 1] = last


# Function to print Sorted Array
def printSortedArray(sortedArray):

    string = "Sorted Array is : "

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

    # Select Sorting type
    sortingType = "Desc"

    # Calling recursive insertion sort function
    RecursiveInsertionSort(unsortedArray, arrayLength, sortingType)

    # Call printArray function to print the sorted array
    printSortedArray(unsortedArray)
