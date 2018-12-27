# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : MergeSort.py
#
# Author            : Ashish
#
# Date created      : 20181220
#
# Purpose           : Implementing merge sort algorithm in python
#
# **********************************************************************;

# Function that implements Merge sort
def mergeSort(unsortedArray):

    if len(unsortedArray) > 1:
        # Finding the mid of the array
        mid = len(unsortedArray) // 2
        # Dividing the array elements
        L = unsortedArray[:mid]

        # into 2 halves
        R = unsortedArray[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                unsortedArray[k] = L[i]
                i = i + 1
            else:
                unsortedArray[k] = R[j]
                j = j + 1
            k = k + 1

        # Checking if any element was left
        while i < len(L):
            unsortedArray[k] = L[i]
            i = i + 1
            k = k + 1

        while j < len(R):
            unsortedArray[k] = R[j]
            j = j + 1
            k = k + 1


# Function to print Sorted Array
def printSortedArray(sortedArray):
    string = ""

    for i in range(len(sortedArray)):
        string += str(sortedArray[i]) + " "

    # Print Sorted array to the console
    print(string)


# Main function that executes when script runs on the console
if __name__ == "__main__":
    # Test values for sorting
    unsortedArray = [12, 11, 13, 5, 6, 7]

    # Calling selection sort function
    mergeSort(unsortedArray)

    # Call printArray function to print the sorted array
    printSortedArray(unsortedArray)
