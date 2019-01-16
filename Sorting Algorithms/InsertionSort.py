# **********************************************************************;
# Project           : Learning Algorithms
# 
# Program name      : insertionSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190113
#
# Purpose           : Implementing insertion sort algorithm in python
#
# **********************************************************************;

class InsertionSort:

    def __init__(self):

        self.unsortedArray = [12, 11, 13, 5, 15, 6, 7, 9, 22, 1]

        self.arraySize = len(self.unsortedArray)

        self.sortingTypeArray = ["Ascending", "ascending", "Asc", "asc"]

    def printArray(self, sortedArray):
        string = ""

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print Sorted array to the console
        print(string)

    # Function that implements insertion sort
    def insertionSort(self, sortingType):

        unsortedArray = self.unsortedArray

        arrayLength = self.arraySize

        for i in range(1, arrayLength):

            # Select the first element in the loop as key
            key = unsortedArray[i]

            j = i - 1

            if sortingType in self.sortingTypeArray:

                # If key value is less then the element at the index then move it.
                while j >= 0 and key < unsortedArray[j]:
                    unsortedArray[j + 1] = unsortedArray[j]
                    j -= 1
            else:
                # If key value is greater then the element at the index then move it.
                while j >= 0 and key > unsortedArray[j]:
                    unsortedArray[j + 1] = unsortedArray[j]
                    j -= 1

            unsortedArray[j + 1] = key

        # Call printArray function to print the sorted array
        self.printArray(unsortedArray)

# Main function that executes when script runs on the console.
if __name__ == "__main__":

    # Select sorting type
    sortingType = "Desc"

    # Create class object
    insert = InsertionSort()

    # Calling insertion sort function
    insert.insertionSort(sortingType)
