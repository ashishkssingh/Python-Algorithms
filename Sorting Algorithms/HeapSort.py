# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : HeapSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20180104
#
# Purpose           : Implementing heap sort algorithm in python
#
# **********************************************************************;

# To heapify subtree rooted at index i
def heapify(unsortedArray, arraySize, i):

    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < arraySize and unsortedArray[i] < unsortedArray[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < arraySize and unsortedArray[largest] < unsortedArray[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        unsortedArray[i], unsortedArray[largest] = unsortedArray[largest], unsortedArray[i]  # swap

        # Heapify the root.
        heapify(unsortedArray, arraySize, largest)

# The main function to sort an array of given size
def heapSort(unsortedArray):
    arraySize = len(unsortedArray)

    # Build a maxheap.
    for i in range(arraySize, -1, -1):
        heapify(unsortedArray, arraySize, i)

    # One by one extract elements
    for i in range(arraySize - 1, 0, -1):
        unsortedArray[i], unsortedArray[0] = unsortedArray[0], unsortedArray[i]  # swap
        heapify(unsortedArray, i, 0)

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
    unsortedArray = [12, 11, 13, 5, 6]

    # Calling insertion sort function
    heapSort(unsortedArray)

    # Print the sorted array
    printSortedArray(unsortedArray)
