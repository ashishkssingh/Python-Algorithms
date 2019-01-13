# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : IterativeMergeSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190113
#
# Purpose           : Implementing iterative merge sort algorithm in python
#
# **********************************************************************;

class IterativeMergeSort:
    # Declare Global Variables
    unsortedArray = []
    sortingTypeArray = []
    arraySize = 0

    # Initialize Global Variables
    def __init__(self):

        # Array that needs to be sorted
        self.unsortedArray = [12, 11, 13, 5, 15, 6, 7, 9, 22, 1]

        # Size of the unsorted array
        self.arraySize = len(self.unsortedArray)

        # Type of sorting to be performed
        self.sortingTypeArray = ["Ascending", "ascending", "asc", "Asc"]

    # Function to print the sorted the array
    def printArray(self, sortedArray):

        string = ""

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print Sorted array to the console
        print(string)

    # Function to implement merge sort algorithm
    def mergeSort(self, sortingType):

        # Make local variable of the unsorted array
        a = self.unsortedArray

        # Set sub array size
        current_size = 1

        # Outer loop for traversing Each sub array of current_size
        while current_size < len(a) - 1:

            left = 0
            # Inner loop for merge call in a sub array, Each complete Iteration sorts the iterating sub array

            while left < len(a) - 1:
                # middle index = minimum of left + current_size - 1 and length of array - 1
                middle = min(left + current_size - 1, len(a) - 1)

                # right index = minimum of 2 * current_size + left - 1 , length of array -1
                right = min(2 * current_size + left - 1, len(a) - 1)

                # Merge call for each sub array
                self.merge(left, middle, right, sortingType)

                # Traverse through the sub arrays
                left = left + current_size * 2

            # Increasing sub array size by multiple of 2
            current_size = 2 * current_size

        # Print sorted array
        self.printArray(self.unsortedArray)

    # Merge function to merge the sorted array into one bigger array
    def merge(self, l, m, r, sortinType):

        # Make a local copy of sorted array
        a = self.unsortedArray

        # Calculate the size of the sub array
        n1 = m - l + 1
        n2 = r - m

        # Create temp array of the calculated size
        Left = [0] * n1
        Right = [0] * n2

        # Copy sorted sub array into left temp array
        for i in range(0, n1):
            Left[i] = a[l + i]

        # Copy the sorted sub array into right temp array
        for i in range(0, n2):
            Right[i] = a[m + i + 1]

        # Initialize variables to copy the elements from temp array back to main array
        i, j, k = 0, 0, l

        # Loop to copy back elements into the main array
        while i < n1 and j < n2:

            if sortingType in self.sortingTypeArray:

                # Condition to copy if the sorting type is ascending
                if Left[i] > Right[j]:
                    a[k] = Right[j]
                    j += 1
                else:
                    a[k] = Left[i]
                    i += 1
                k += 1

            else:

                # Condition to copy if the sorting type is descending
                if Left[i] < Right[j]:
                    a[k] = Right[j]
                    j += 1
                else:
                    a[k] = Left[i]
                    i += 1
                k += 1

        # Copy remaining element into the array
        while i < n1:
            a[k] = Left[i]
            i += 1
            k += 1

        while j < n2:
            a[k] = Right[j]
            j += 1
            k += 1


if __name__ == "__main__":
	
    # Select sorting type
    sortingType = "desc"

    # Create class object of merge sort
    iMerge = IterativeMergeSort()

    # Call the sorting function
    iMerge.mergeSort(sortingType)
