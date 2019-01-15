# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : ExponentialSearch.py
#
# Author            : Ashish Singh
#
# Date created      : 20190114
#
# Purpose           : Implementing Exponential Search algorithm in python
#
# **********************************************************************;

class ExponentialSearch:

    def __init__(self):

        # Initialize searching array
        self.searchArray = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

        # Value to be searched in the array
        self.searchedValue = 144

        # Size of the searching array
        self.arraySize = len(self.searchArray)

    # Function that implements the search algorithm
    def binarySearch(self, arr, l, r, x):
        if r >= l:
            mid = l + (r - l) / 2

            # If the element is present at
            # the middle itself
            if arr[mid] == x:
                return mid

            # If the element is smaller than mid,
            # then it can only be present in the
            # left subarray
            if arr[mid] > x:
                return self.binarySearch(arr, l,
                                    mid - 1, x)

            # Else he element can only be
            # present in the right
            return self.binarySearch(arr, mid + 1, r, x)

        # We reach here if the element is not present
        return -1

    # Returns the position of first occurence of x in array
    def exponentialSearch(self, arr, n, x):
        # IF x is present at first
        # location itself
        if arr[0] == x:
            return 0

        # Find range for binary search
        # j by repeated doubling
        i = 1
        while i < n and arr[i] <= x:
            i = i * 2

        # Call binary search for the found range
        return self.binarySearch(arr, i / 2,
                            min(i, n), x)

    # Function to print index of the element
    def printIndex(self, index):
        # Check for the value of the index, if -1 the value was not found else print the value of index
        if index == -1:
            print("Value was not found in the array")
        else:
            print("Value was found at index : " + str(index))


# Main function that executes when script runs on the console.
if __name__ == "__main__":

    expo = ExponentialSearch()

    index = expo.exponentialSearch(expo.searchArray, expo.arraySize, expo.searchedValue)

    expo.printIndex(index)
