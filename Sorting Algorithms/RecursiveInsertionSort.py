# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : RecursiveInsertionSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190111
#
# Purpose           : Implementing recursive insertion sort algorithm in python
#
# **********************************************************************;

class RecursiveInsertionSort:

    def __init__(self):

        # Array to be sorted
        self.unsortedArray = [18, 75, 77, 70, 32, 15, 71, 64, 67, 14]

        # Size of the array
        self.arraySize = len(self.unsortedArray)

        # Array of sorting type
        self.sortingArrayType = ["Ascending", "ascending", "Asc", "asc"]

    def printArray(self, sortedArray):
        string = "Sorted Array is : "

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print Sorted array to the console
        print(string)

    def recursiveInsertionSort(self, sortingType, arraySize):

        # Make local copy of global array
        unsortedArray = self.unsortedArray

        # Base case to exit out of the recursion loop
        if arraySize <= 1:
            return 0

        # Sort first n-1 elements
        self.recursiveInsertionSort(sortingType, arraySize - 1)

        # Insert the last element in the correct position and use it as key
        last = unsortedArray[arraySize - 1]
        j = arraySize - 2

        if sortingType in self.sortingArrayType:

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


# Main function that executes when script runs on the console.
if __name__ == "__main__":

    # Select Sorting type
    sortingType = "asc"

    # Create Insertion sort object
    recursive_insert = RecursiveInsertionSort()

    # Calling recursive insertion sort function
    recursive_insert.recursiveInsertionSort(sortingType, recursive_insert.arraySize)

    # Call printArray function to print the sorted array
    recursive_insert.printArray(recursive_insert.unsortedArray)
