# Function to calculate the partitioning element
def partition(unsortedArray, low, high):

    # start from value lower than the starting index
    i = low - 1

    # Consider pivoting element to be the last element in the array
    pivot = unsortedArray[high]

    # Loop though all the elements of the array
    for j in range(low, high):

        # Compare each element with the pivot, only if it is less than pivot element move it to [i] position
        if unsortedArray[j] <= pivot:
            i = i + 1
            unsortedArray[i], unsortedArray[j] = unsortedArray[j], unsortedArray[i]

    # when the loop ends place the pivot element in the right position
    unsortedArray[i+1], unsortedArray[high] = unsortedArray[high], unsortedArray[i+1]

    # return the pivot position
    return i+1

# Function that implements quick sort algorithm
def quicksort(unsortedArray, low, high):

    # Check if array has element or not
    if low < high:

        # Call partitioning function to get the partition index
        pi = partition(unsortedArray, low, high)

        # Call quick sort function with lower limit as start index and last index as one index behind pivot
        quicksort(unsortedArray, low, pi - 1)

        # Call quick sort function with lower limit as one index above the pivot and last index as the last index
        quicksort(unsortedArray, pi+1, high)

# Function to print the sorted array
def printArray(sortedArray, arraySize):

    string = "Sorted Array is : "

    for i in range(arraySize):
        string += str(sortedArray[i])+" "
    # Print the sorted array
    print(string)

# Main function that will be called when executed from console
if __name__ == "__main__":

    # Array that needs to be sorted
    unsortedArray = [10, 7, 8, 9, 1, 5]

    # Getting size of the array
    arraySize = len(unsortedArray)

    # Call the quick sort function with required arguments
    quicksort(unsortedArray, 0, arraySize-1)

    # Call the print function to print sorted array
    printArray(unsortedArray, arraySize)