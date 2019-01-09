# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : selectionSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190109
#
# Purpose           : Implementing selection sort algorithm in python
#
# **********************************************************************;

# Function that implements Selection sort
def selectionSort(unsortedArray, sortingType):
    # get length of the array
    arrayLength = len(unsortedArray)

    # Loop throught all elements of the array
    for i in range(arrayLength):

        # Set the first element of the loop as the smallest element and store its index
        smallestValueIndex = i

        # inner loop to compare with every other elements, leaving the selected element index
        for j in range(i + 1, arrayLength):

            # If the any other values is less than previous, set new minimum index
            if (unsortedArray[smallestValueIndex] > unsortedArray[j]):
                smallestValueIndex = j

        if sortingType == "Ascending":
            unsortedArray[i], unsortedArray[smallestValueIndex] = unsortedArray[smallestValueIndex], unsortedArray[i]
        else:
            unsortedArray[arrayLength-1-i], unsortedArray[smallestValueIndex] = unsortedArray[smallestValueIndex], unsortedArray[arrayLength-1-i]

    # Call printArray function to print the sorted array
    printSortedArray(unsortedArray)


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
    unsortedArray = [18, 75, 77, 70, 32, 15, 71, 64, 67, 14]

    # Type of sorting to be performed Ascending or Descending
    sortingType = "Descending"

    # Calling selection sort function
    selectionSort(unsortedArray, sortingType)
