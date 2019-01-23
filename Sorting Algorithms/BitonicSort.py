# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : BitonicSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190120
#
# Purpose           : Implementing Bitonic Sort algorithm in python 3
#
# **********************************************************************;

class Bitonic:

    # Function to initialize global variables
    def __init__(self):

        # Array to be sorted
        self.unsortedArray = [18, 75, 77, 70, 32, 15, 71, 64, 67, 14]

        # Size of the unsorted array
        self.arraySize = len(self.unsortedArray)

        # Type of sorting to be performed
        self.sortingTypeArray = ["ascending", "asc"]

    # Function to print the sorted array
    def printArray(self, sortedArray):

        string = "Sorted Array is : "

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print the sorted array
        print(string)

    def compAndSwap(self, a, i, j, dire):
        if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
            a[i], a[j] = a[j], a[i]

    """ 
    It recursively sorts a bitonic sequence in ascending order,if dir = 1, and in descending order
    otherwise (means dir=0). The sequence to be sorted starts at index position low, the parameter cnt is the
    number of elements to be sorted.
    """

    def bitonicMerge(self, a, low, cnt, dire):
        if cnt > 1:
            k = int(cnt / 2)
            for i in range(low, low + k):
                self.compAndSwap(a, i, i + k, dire)
            self.bitonicMerge(a, low, k, dire)
            self.bitonicMerge(a, low + k, k, dire)

    """ 
    This function first produces a bitonic sequence by recursively sorting its two halves in opposite sorting orders,
    and then calls Bitonic Merge to make them in the same order 
    """

    def bitonicSort(self, a, low, cnt, dire):
        if cnt > 1:
            k = int(cnt / 2)
            self.bitonicSort(a, low, k, 1)
            self.bitonicSort(a, low + k, k, 0)
            self.bitonicMerge(a, low, cnt, dire)

    # Caller of bitonicSort for sorting the entire array of length N in ASCENDING order
    def sort(self, a, N, sortingType):

        if sortingType in self.sortingTypeArray:
            up = 1
        else:
            up = 0

        self.bitonicSort(a, 0, N, up)


# Main function that will be called when executed from console.
if __name__ == "__main__":
    # Select the type of sorting
    sortingType = "asc"

    # Creating object of the class
    bit = Bitonic()

    # Calling sort function from the class object
    bit.sort(bit.unsortedArray, bit.arraySize, sortingType)

    # Call the print function to print sorted array
    bit.printArray(bit.unsortedArray)
