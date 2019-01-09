# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : ShellSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190108
#
# Purpose           : Implementing shell sort algorithm in python
#
# **********************************************************************;

# Function to implement shell sort algorithm
def shellSort(arr):

    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n // 2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2

    printSortedArray(arr)


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
    unsortedArray = [59, 84, 4, 50,	86,	97,	21,	71,	92]

    # Calling insertion sort function
    shellSort(unsortedArray)
