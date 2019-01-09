# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : BubbleSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190109
#
# Purpose           : Implementing bubble sort algorithm in python
#
# **********************************************************************;

# Function that implements Bubble sort
def bubbleSort(unsortedArray, sortingType):

    # get length of the array
    arrayLength = len(unsortedArray)

    # Loop through all elements of the array
    for i in range(arrayLength):

        # inner loop to compare with every other elements
        for j in range(arrayLength - i - 1):

            if sortingType == "Ascending" or sortingType == "ascending" or sortingType == "asc" or sortingType == "Asc":
                # If the next values is less than previous, interchange them
                if unsortedArray[j] > unsortedArray[j + 1]:
                    unsortedArray[j], unsortedArray[j + 1] = unsortedArray[j + 1], unsortedArray[j]
            else:
                # If the next values is greater than previous, interchange them
                if unsortedArray[j] < unsortedArray[j + 1]:
                    unsortedArray[j], unsortedArray[j + 1] = unsortedArray[j + 1], unsortedArray[j]

    # Call printArray function to print the sorted array
    printArray(unsortedArray)


# Function to print Sorted Array
def printArray(sortedArray):
    string = ""

    for i in range(len(sortedArray)):
        string += str(sortedArray[i]) + " "

    # Print Sorted array to the console
    print(string)


# Main function that executes when script runs on the console.
if __name__ == "__main__":
    # Test values for sorting
    unsortedArray = [64, 34, 25, 12, 22, 11, 90]

    # Type of sorting to be performed Ascending or Descending
    sortingType = "asc"

    # Calling bubble sort function
    bubbleSort(unsortedArray, sortingType)
