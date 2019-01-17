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

class ShellSort:

    def __init__(self):

        # Test values for sorting
        self.unsortedArray = [59, 84, 4, 50, 86, 97, 21, 71, 92]

        # Type of Sorting to be performed
        self.sortingTypeArray = ["Ascending", "ascending", "Asc", "asc"]

    # Function to print Sorted Array
    def printArray(self, sortedArray):
        string = ""

        for i in range(len(sortedArray)):
            string += str(sortedArray[i]) + " "

        # Print Sorted array to the console
        print(string)

    # Function to implement shell sort algorithm
    def shellSort(self, unsortedArray, sortingType):

        # Start with a big gap, then reduce the gap
        n = len(unsortedArray)
        gap = n // 2

        # Do a gapped insertion sort for this gap size.
        # The first gap elements a[0..gap-1] are already in gapped
        # order keep adding one more element until the entire array
        # is gap sorted
        while gap > 0:

            for i in range(gap, n):

                # add a[i] to the elements that have been gap sorted
                # save a[i] in temp and make a hole at position i
                temp = unsortedArray[i]

                # shift earlier gap-sorted elements up until the correct
                # location for a[i] is found
                j = i
                while j >= gap and unsortedArray[j - gap] > temp:
                    unsortedArray[j] = unsortedArray[j - gap]
                    j -= gap

                    # put temp (the original a[i]) in its correct location
                    unsortedArray[j] = temp
            gap //= 2


# Main function that executes when script runs on the console.
if __name__ == "__main__":

    # Select the sorting type
    sortingType = "desc"

    # Create object of the class
    shell = ShellSort()

    # Calling insertion sort function
    shell.shellSort(shell.unsortedArray, sortingType)

    # Call the print function to print the sorted Array
    shell.printArray(shell.unsortedArray)
