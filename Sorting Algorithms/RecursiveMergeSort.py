# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : RecursiveMergeSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20181226
#
# Purpose           : Implementing recursive merge sort algorithm in python
#
# **********************************************************************;

# Function that implements Selection sort
def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergeSort(list):

    if len(list) < 2:
        return list

    middle = len(list) / 2
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])

    return merge(left, right)


# Function to print Sorted Array
def printSortedArray(sortedArray):
    string = ""

    for i in range(len(sortedArray)):
        string += str(sortedArray[i]) + " "

    # Print Sorted array to the console
    print(string)


# Main function that executes when script runs on the console
if __name__ == "__main__":

    # Test values for sorting
    unsortedArray = [12, 11, 13, 5, 6, 7]

    # Calling selection sort function
    sortedArray = mergeSort(unsortedArray)

    # Call printArray function to print the sorted array
    printSortedArray(sortedArray)
