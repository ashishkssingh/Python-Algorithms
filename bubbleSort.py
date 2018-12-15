# **********************************************************************;
# Project           : Learning Algorithms
# 
# Program name      : bubbleSort.py
#
# Author            : Ashish
#
# Date created      : 20181215
#
# Purpose           : Implementing bubble sort algorithm in python
#
#**********************************************************************;

def bubbleSort(unsortedArray):

	arrayLength = len(unsortedArray)

	for i in range(arrayLength):

		for j in range(arrayLength - i - 1):

			if unsortedArray[j] > unsortedArray[j+1]:
				unsortedArray[j],unsortedArray[j+1] = unsortedArray[j+1],unsortedArray[j]

	printArray(unsortedArray)

def printArray(sortedArray):

	string = ""

	for i in range(len(sortedArray)):
		string += str(sortedArray[i]) + " "

	print(string)

if __name__ == "__main__":
    """ This is executed when run from the command line """

    unsortedArray = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(unsortedArray)