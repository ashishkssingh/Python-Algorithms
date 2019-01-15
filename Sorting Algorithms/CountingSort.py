# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : CountingSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190106
#
# Purpose           : Implementing Counting sort algorithm in python
#
# **********************************************************************;

class CountingSort:

    def __init__(self):

        # Test values for sorting
        self.unsortedArray = [170, 45, 75, 90, 802, 24, 2, 66]

        self.max1 = max(self.unsortedArray)

        self.sortingTypeArray = ["Ascending", "ascending", "Asc", "asc"]

    # A function to do counting sort of arr[] according to the digit represented by exponent.
    def countingSort(self, unsortedArray, exponent, sortingType):

        arraySize = len(unsortedArray)

        # The output array elements that will have sorted arr
        output = [0] * arraySize

        # initialize count array as 0
        count = [0] * 10

        # Store count of occurrences in count[]
        for i in range(0, arraySize):
            index = int(unsortedArray[i] / exponent)
            count[index % 10] += 1

        # Change count[i] so that count[i] now contains actual position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = arraySize - 1
        while i >= 0:
            index = int(unsortedArray[i] / exponent)
            output[count[index % 10] - 1] = unsortedArray[i]
            count[index % 10] -= 1
            i -= 1

        # Copying the output array to arr[],so that arr now contains sorted numbers

        if sortingType in self.sortingTypeArray:
            for i in range(0, len(unsortedArray)):
                unsortedArray[i] = output[i]
        else:
            for i in range(len(unsortedArray)-1, -1, -1):
                unsortedArray[i] = output[i]

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

    count = CountingSort()

    # Calling insertion sort function
    exponent = 1
    while count.max1 / exponent > 0:
        count.countingSort(count.unsortedArray, exponent, sortingType)
        exponent *= 10

    # Call print function to print sorted array
    count.printArray(count.unsortedArray)
