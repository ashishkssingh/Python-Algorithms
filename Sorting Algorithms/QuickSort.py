# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : QuickSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190112
#
# Purpose           : Implementing Quick Sort algorithm in python 3
#
# **********************************************************************;

class QuickSort:

    # Declare global variables
    unsortedArray = []
    sortingArrayType = []
    arraySize = 0

    # Function to initialize global variables
    def __init__(self):

        # Array to be sorted
        self.unsortedArray = [18, 75, 77, 70, 32, 15, 71, 64, 67, 14]

        # Size of the unsorted array
        self.arraySize = len(self.unsortedArray)

        # Type of sorting to be performed
        self.sortingTypeArray = ["Ascending", "ascending", "Asc", "asc"]

    # Function to print the sorted array
    def printArray(self, sortedArray):

        string = "Sorted Array is : "

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print the sorted array
        print(string)

    # Function to find the partition element from the array
    def partition(self, unsortedArray, low, high, sortingType):

        # Set the counter value as -1
        i = low - 1

        # Consider the highest element of the array as the pivot element
        pivot = self.unsortedArray[high]

        # Loop through all elements of the array
        for j in range(low, high):

            # If type of sorting is ascending
            if sortingType in self.sortingTypeArray:

                # If array element is less the pivot element then place it on (i)th index
                if unsortedArray[j] < pivot:
                    i = i + 1
                    unsortedArray[i], unsortedArray[j] = unsortedArray[j], unsortedArray[i]

            else:

                # If array element is greater the pivot element then place it on (i)th index
                if unsortedArray[j] > pivot:
                    i = i + 1
                    unsortedArray[i], unsortedArray[j] = unsortedArray[j], unsortedArray[i]

        # After traversing all the elements in the array place the pivot element on the (i+1)th index
        unsortedArray[i+1], unsortedArray[high] = unsortedArray[high], unsortedArray[i+1]

        # return the changed pivot index
        return i + 1

    # Function to implement quick sort algorithm
    def quickSort(self, unsortedArray, low, high, sortingType):

        # Check if the array length is less than 2
        if low < high:

            # Call partition function to get pivot index
            pi = self.partition(unsortedArray, low, high, sortingType)

            # Call quicksort function on the left subset of the array
            self.quickSort(unsortedArray, low, pi - 1, sortingType)

            # Call quicksort function on right subset of the array
            self.quickSort(unsortedArray, pi + 1, high, sortingType)


# Main function that will be called when executed from console.
if __name__ == "__main__":

    # Select the type of sorting
    sortingType = "desc"

    # Creating object of the class
    quick = QuickSort()

    # Calling sort function from the class object
    quick.quickSort(quick.unsortedArray, 0, len(quick.unsortedArray)-1, sortingType)

    # Call the print function to print sorted array
    quick.printArray(quick.unsortedArray)
