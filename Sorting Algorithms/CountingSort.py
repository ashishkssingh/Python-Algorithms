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

# A function to do counting sort of arr[] according to the digit represented by exponent.
def countingSort(unsortedArray, exponent):

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
    i = 0
    for i in range(0, len(unsortedArray)):
        unsortedArray[i] = output[i]



# Function to print Sorted Array
def printSortedArray(sortedArray):

    string = ""

    for i in range(len(sortedArray)):
        string += str(sortedArray[i]) + " "

    # Print Sorted array to the console
    print(string)


# Main function that executes when script runs on the console.
if __name__ == "__main__":

    # Test values for sorting
    unsortedArray = [ 170, 45, 75, 90, 802, 24, 2, 66]

    max1 = max(unsortedArray)

    # Calling insertion sort function
    exponent = 1
    while max1 / exponent > 0:
        countingSort(unsortedArray, exponent)
        exponent *= 10

    # Call print function to print sorted array
    printSortedArray(unsortedArray)
