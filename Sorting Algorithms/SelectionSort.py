# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : selectionSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190110
#
# Purpose           : Implementing selection sort algorithm in python
#
# **********************************************************************;

# Class to implement selection sort algorithm
class SelectionSort:

    # Variable initialization
    unsortedArray = []
    arraySize = 0
    sortingTypeArray = []

    # Function to define global variables
    def __init__(self):

        # Array to be sorted
        self.unsortedArray = [18, 75, 77, 70, 32, 15, 71, 64, 67, 14]

        # Size of the array
        self.arraySize = len(self.unsortedArray)

        # Array of sorting type
        self.sortingTypeArray = ["asc", "Asc", "Ascending", "ascending"]

    # Function to print the sorted array
    def printArray(self,sortedArray):
        string = ""

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print Sorted array to the console
        print(string)

    # Function to implement selection sort algorithm
    def selectionSort(self, sortingType, arraySize):

        # Make a local variable of the unsorted array
        unsortedArray = self.unsortedArray

        # Loop through all the elements in the array
        for i in range(arraySize):

            # Set the first element of the loop as the smallest element and store its index
            firstIndex = i

            # inner loop to compare with every other elements, leaving the selected element index
            for j in range(i + 1, arraySize):

                if sortingType in self.sortingTypeArray:

                    # If the any other values is less than previous, set new minimum index
                    if (unsortedArray[firstIndex] > unsortedArray[j]):
                        firstIndex = j
                else:

                    # If the any other values is greater than previous, set new maximum index
                    if (unsortedArray[firstIndex] < unsortedArray[j]):
                        firstIndex = j

            # Swap the maximum or the minimum element found with the index selected
            unsortedArray[i], unsortedArray[firstIndex] = unsortedArray[firstIndex], unsortedArray[i]

        # Call printArray function to print the sorted array
        self.printArray(unsortedArray)

if __name__ == "__main__":

    # Select sorting type
    sortingType = "desc"

    # Create object of the Selection Sort function
    selection = SelectionSort()

    # Call the seleciton sort function from the class object
    selection.selectionSort(sortingType, selection.arraySize)
