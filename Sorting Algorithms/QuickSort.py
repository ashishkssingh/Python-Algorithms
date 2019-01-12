# **********************************************************************;
# Project           : Learning Algorithms
# 
# Program name      : QuickSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20181217
#
# Purpose           : Implementing Quick Sort algorithm in python 3
#
# **********************************************************************;

class QuickSort:

    unsortedArray = []
    sortingArrayType = []
    arraySize = 0

    def __init__(self):

        self.unsortedArray = [18, 75, 77, 70, 32, 15, 71, 64, 67, 14]

        self.arraySize = len(self.unsortedArray)

        self.sortingTypeArray = ["Ascending", "ascending", "Asc", "asc"]

    def printArray(self, sortedArray):

        string = "Sorted Array is : "

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print the sorted array
        print(string)

    def partition(self, unsortedArray, low, high, sortingType):

        i = low - 1

        pivot = self.unsortedArray[high]

        for j in range(low, high):

            if sortingType in self.sortingTypeArray:

                if unsortedArray[j] < pivot:
                    i = i + 1
                    unsortedArray[i], unsortedArray[j] = unsortedArray[j], unsortedArray[i]

            else:

                if unsortedArray[j] > pivot:
                    i = i + 1
                    unsortedArray[i], unsortedArray[j] = unsortedArray[j], unsortedArray[i]

        unsortedArray[i+1], unsortedArray[high] = unsortedArray[high], unsortedArray[i+1]

        return i + 1

    def quickSort(self, unsortedArray, low, high, sortingType):

        if low < high:

            pi = self.partition(unsortedArray, low, high, sortingType)

            self.quickSort(unsortedArray, low, pi - 1, sortingType)

            self.quickSort(unsortedArray, pi + 1, high, sortingType)


# Main function that will be called when executed from console.
if __name__ == "__main__":

    sortingType = "desc"

    # Creating object of the class
    quick = QuickSort()

    # Calling sort function from the class object
    quick.quickSort(quick.unsortedArray, 0, len(quick.unsortedArray)-1, sortingType)

    # Call the print function to print sorted array
    quick.printArray(quick.unsortedArray)
