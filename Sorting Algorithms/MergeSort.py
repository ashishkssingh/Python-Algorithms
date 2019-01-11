# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : MergeSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190111
#
# Purpose           : Implementing merge sort algorithm in python
#
# **********************************************************************;

class MergeSort:
    # Declare Global Variables
    unsortedArray = []
    sortingTypeArray = []
    arraySize = 0

    # Function to initialize the global variables
    def __init__(self):

        self.unsortedArray = [18, 75, 77, 70, 32, 15, 71, 64, 67, 14]

        self.sortingTypeArray = ["Asc", "asc", "Ascending", "ascending"]

        self.arraySize = len(self.unsortedArray)

    def printArray(self, sortedArray):
        string = ""

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print Sorted array to the console
        print(string)

    # Function that implements Merge sort
    def mergeSort(self, unsortedArray):

        # Sort only if the size of the array is greater than 1
        if len(unsortedArray) > 1:

            # Find the center element of the array
            middle = len(unsortedArray) // 2

            # Find the left subset of the array
            left = unsortedArray[:middle]

            # Find the right subset of the array
            right = unsortedArray[middle:]

            # Recursively call merge sort on the left subset
            self.mergeSort(left)

            # Recursively call merge sort on the right subset
            self.mergeSort(right)

            i = j = k = 0

            # Copy data to temp arrays L[] and R[]
            while i < len(left) and j < len(right):

                if sortingType in self.sortingTypeArray:
                    if left[i] < right[j]:
                        unsortedArray[k] = left[i]
                        i = i + 1
                    else:
                        unsortedArray[k] = right[j]
                        j = j + 1
                    k = k + 1
                else:
                    if left[i] > right[j]:
                        unsortedArray[k] = left[i]
                        i = i + 1
                    else:
                        unsortedArray[k] = right[j]
                        j = j + 1
                    k = k + 1

            # Checking if any element was left
            while i < len(left):
                unsortedArray[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                unsortedArray[k] = right[j]
                j = j + 1
                k = k + 1


# Main function that executes when script runs on the console
if __name__ == "__main__":

    # Select sorting type
    sortingType = "Desc"

    # Create object of class
    merge = MergeSort()

    # Call merge sort function from class object
    merge.mergeSort(merge.unsortedArray)

    # Call print function from the class object
    merge.printArray(merge.unsortedArray)
