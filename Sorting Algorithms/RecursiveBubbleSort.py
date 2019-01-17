# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : RecursiveBubbleSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190110
#
# Purpose           : Implementing bubble sort algorithm in python
#
# **********************************************************************;

class RecursiveBubbleSort:

    # Function to initialize global values
    def __init__(self):

        # Array to be sorted using bubble sort
        self.unsortedArray = [54, 89, 43, 36, 34, 100, 56, 39, 56, 31]

        # Size of array
        self.arraySize = len(self.unsortedArray)

        # Sorting type to be implemented
        self.sortingTypeArray = ["Ascending", "ascending", "asc", "Asc"]

    # Function to print sorted array
    def printArray(self, sortedArray):
        string = "Sorted array is : "

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print Sorted array to the console
        print(string)

    # Function that implements recursive bubble sort
    def recursiveBubbleSort(self, sortingType, arraySize):

        # Initialize the array to a local variable
        unsortedArray = self.unsortedArray

        # Base case to terminate the recursion
        if arraySize == 1:
            self.printArray(self.unsortedArray)
            return 0

        # Loop through all elements in the array
        for i in range(arraySize - 1):

            if sortingType in self.sortingTypeArray:
                # If the next values is less than previous, interchange them
                if unsortedArray[i] > unsortedArray[i + 1]:
                    unsortedArray[i], unsortedArray[i + 1] = unsortedArray[i + 1], unsortedArray[i]

            else:
                # If the next values is greater than previous, interchange them
                if unsortedArray[i] < unsortedArray[i + 1]:
                    unsortedArray[i], unsortedArray[i + 1] = unsortedArray[i + 1], unsortedArray[i]

        self.recursiveBubbleSort(sortingType, arraySize - 1)


if __name__ == "__main__":
    # Initialize the sorting type
    sortingType = "desc"

    # Create the object for the sorting function
    recursive_bubble = RecursiveBubbleSort()

    # Call the sorting functino from the object
    recursive_bubble.recursiveBubbleSort(sortingType, recursive_bubble.arraySize)