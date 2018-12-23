# **********************************************************************;
# Project           : Learning Algorithms
# 
# Program name      : RecursiveBubbleSort.py
#
# Author            : Ashish
#
# Date created      : 20181223
#
# Purpose           : Implementing bubble sort algorithm in python
#
#**********************************************************************;

# Function that implements Bubble sort
def RecursiveBubbleSort(unsortedArray, n):
    
    #  Base case 
    if n == 1:
        
        # Call printArray function to print the sorted array
        printArray(unsortedArray)
        return 0
        
    # Loop throught all elements of the array
    for i in range(n-1):
        
        # If the next values is less than previous, interchange them
        if unsortedArray[i] > unsortedArray[i+1]:
            unsortedArray[i],unsortedArray[i+1] = unsortedArray[i+1],unsortedArray[i]
                
    RecursiveBubbleSort(unsortedArray, n-1)

# Function to print Sorted Array
def printArray(sortedArray):

	string = "Sorted array is : "

	for i in range(len(sortedArray)):
		string += str(sortedArray[i]) + " "

	# Print Sorted array to the console
	print(string)

# Main function that executes when script runs on the console.
if __name__ == "__main__":
    
    # Test values for sorting
    unsortedArray = [64, 34, 25, 12, 22, 11, 90]
    
    # get length of the array
    arrayLength = len(unsortedArray)
    
    # Calling bubble sort function
    RecursiveBubbleSort(unsortedArray,arrayLength)
