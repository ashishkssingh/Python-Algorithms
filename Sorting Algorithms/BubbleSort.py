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


class BubbleSort:

    def __init__(self):

        # Test values for sorting
        self.unsortedArray = [54, 89, 43, 36, 34, 100, 56, 39, 56, 31]

        self.sortingTypeArray = ["Ascending", "ascending", "asc", "Asc"]

    # Function that implements Bubble sort
    def bubbleSort(self, sortingType):

        unsortedArray = self.unsortedArray

        sortingTypeArray = self.sortingTypeArray

        # get length of the array
        arrayLength = len(unsortedArray)

        # Loop through all elements of the array
        for i in range(arrayLength):

            # inner loop to compare with every other elements
            for j in range(arrayLength - i - 1):

                if (sortingType in sortingTypeArray):
                    # If the next values is less than previous, interchange them
                    if unsortedArray[j] > unsortedArray[j + 1]:
                        unsortedArray[j], unsortedArray[j + 1] = unsortedArray[j + 1], unsortedArray[j]
                else:
                    # If the next values is greater than previous, interchange them
                    if unsortedArray[j] < unsortedArray[j + 1]:
                        unsortedArray[j], unsortedArray[j + 1] = unsortedArray[j + 1], unsortedArray[j]

        # Call printArray function to print the sorted array
        self.printArray(unsortedArray)

    # Function to print Sorted Array
    def printArray(self, sortedArray):
        string = ""

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print Sorted array to the console
        print(string)


# Main function that executes when script runs on the console.
if __name__ == "__main__":

    # Type of sorting to be performed Ascending or Descending
    sortingType = "asc"

    # Create object of bubble sort class
    bubble = BubbleSort()

    # Calling bubble sort function
    bubble.bubbleSort(sortingType)
