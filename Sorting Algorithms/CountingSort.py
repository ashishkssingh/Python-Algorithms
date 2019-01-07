# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : CountingSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20180106
#
# Purpose           : Implementing Counting sort algorithm in python
#
# **********************************************************************;

# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = int(arr[i] / exp1)
        count[(index) % 10] += 1

    # Change count[i] so that count[i] now contains actual position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = int(arr[i] / exp1)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    # Copying the output array to arr[],so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]



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
    exp = 1
    while max1 / exp > 0:
        countingSort(unsortedArray, exp)
        exp *= 10

    # Print the sorted array
    printSortedArray(unsortedArray)
