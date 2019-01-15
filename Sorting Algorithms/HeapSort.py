# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : HeapSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190115
#
# Purpose           : Implementing heap sort algorithm in python
#
# **********************************************************************;

class HeapSort:

    def __init__(self):

        self.unsortedArray = [18, 75, 77, 70, 32, 15, 71, 64, 67, 14]

        self.arraySize = len(self.unsortedArray)

        self.sortingTypeArray = ["Ascending", "ascending", "Asc", "asc"]

    # To heapify subtree rooted at index i
    def heapify(self, unsortedArray, arraySize, i, sortingType):

        swapValue = i  # Initialize largest as root
        left = 2 * i + 1  # left node = 2*i + 1
        right = 2 * i + 2  # right node= 2*i + 2

        if sortingType in self.sortingTypeArray:

            # See if left child of root exists and is greater than root
            if left < arraySize and unsortedArray[i] < unsortedArray[left]:
                swapValue = left

            # See if right child of root exists and is greater than root
            if right < arraySize and unsortedArray[swapValue] < unsortedArray[right]:
                swapValue = right

        else:

            # See if left child of root exists and is less than root
            if left < arraySize and unsortedArray[i] > unsortedArray[left]:
                swapValue = left

            # See if right child of root exists and is less than root
            if right < arraySize and unsortedArray[swapValue] > unsortedArray[right]:
                swapValue = right

        # Change root, if needed
        if swapValue != i:
            # Swap the elements
            unsortedArray[i], unsortedArray[swapValue] = unsortedArray[swapValue], unsortedArray[i]

            # Heapify the root node
            self.heapify(unsortedArray, arraySize, swapValue, sortingType)

    # The main function to sort an array of given size
    def heapSort(self, unsortedArray, sortingType):
        arraySize = len(unsortedArray)

        # Build a maxheap
        for i in range(arraySize, -1, -1):
            self.heapify(unsortedArray, arraySize, i, sortingType)

        # One by one extract elements from array and put it into heap
        for i in range(arraySize - 1, 0, -1):
            # Swap the elements
            unsortedArray[i], unsortedArray[0] = unsortedArray[0], unsortedArray[i]
            self.heapify(unsortedArray, i, 0, sortingType)

    # Function to print Sorted Array
    def printArray(self, sortedArray):
        string = ""

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print Sorted array to the console
        print(string)


# Main function that executes when script runs on the console.
if __name__ == "__main__":

    sortingType = "desc"

    # Create object for the class
    heap = HeapSort()

    # Calling insertion sort function
    heap.heapSort(heap.unsortedArray, sortingType)

    # Print the sorted array
    heap.printArray(heap.unsortedArray)
