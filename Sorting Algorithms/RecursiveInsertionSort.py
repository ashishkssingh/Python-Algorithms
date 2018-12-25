# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : RecursiveInsertionSort.py
#
# Author            : Ashish
#
# Date created      : 20181216
#
# Purpose           : Implementing recursive insertion sort algorithm in python
#
# **********************************************************************;

# Function that implements insertion sort
def RecursiveInsertionSort(unsortedArray, arrayLength):

    # base case
    if arrayLength <= 1:
        return

    # Sort first n-1 elements
    RecursiveInsertionSort(unsortedArray, arrayLength - 1)

    '''Insert last element at its correct position 
        in sorted array.'''
    last = unsortedArray[arrayLength - 1]
    j = arrayLength - 2

    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while j >= 0 and unsortedArray[j] > last:
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
    unsortedArray = [12, 11, 13, 5, 6]

    # get length of the array
    arrayLength = len(unsortedArray)

    # Calling insertion sort function
    RecursiveInsertionSort(unsortedArray, arrayLength)

    # Call printArray function to print the sorted array
    printSortedArray(unsortedArray)
