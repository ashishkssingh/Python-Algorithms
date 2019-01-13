# **********************************************************************;
# Project           : Learning Algorithms
#
# Program name      : IterativeMergeSort.py
#
# Author            : Ashish Singh
#
# Date created      : 20190113
#
# Purpose           : Implementing iterative merge sort algorithm in python
#
# **********************************************************************;

class IterativeMergeSort:

	unsortedArray = []
	sortingTypeArray = []
	arraySize = 0

	def __init__(self):

		self.unsortedArray = [12, 11, 13, 5, 15, 6, 7, 9, 22, 1]

		self.arraySize = len(self.unsortedArray)

		self.sortingTypeArray = ["Ascending", "ascending", "asc", "Asc"]

	# Function to print the sorted the array
	def printArray(self, sortedArray):
		string = ""

		for i in range(len(sortedArray)):
			string += str(sortedArray[i]) + " "

		# Print Sorted array to the console
		print(string)

	def mergeSort(self, a):

		current_size = 1

		# Outer loop for traversing Each
		# sub array of current_size
		while current_size < len(a) - 1:

			left = 0
			# Inner loop for merge call
			# in a sub array
			# Each complete Iteration sorts
			# the iterating sub array
			while left < len(a) - 1:
				# mid index = left index of
				# sub array + current sub
				# array size - 1
				mid = min(left + current_size - 1,len(a)-1)

				# (False result,True result)
				# [Condition] Can use current_size
				# if 2 * current_size < len(a)-1
				# else len(a)-1
				right = min(2 * current_size + left - 1, len(a) - 1)

				# Merge call for each sub array
				self.merge(a,left, mid, right)
				left = left + current_size * 2

			# Increasing sub array size by
			# multiple of 2
			current_size = 2 * current_size

		self.printArray(self.unsortedArray)

	# Merge Function
	def merge(self,a, l, m, r):

		n1 = m - l + 1
		n2 = r - m
		L = [0] * n1
		R = [0] * n2
		for i in range(0, n1):
			L[i] = a[l + i]
		for i in range(0, n2):
			R[i] = a[m + i + 1]

		i, j, k = 0, 0, l
		while i < n1 and j < n2:
			if L[i] > R[j]:
				a[k] = R[j]
				j += 1
			else:
				a[k] = L[i]
				i += 1
			k += 1

		while i < n1:
			a[k] = L[i]
			i += 1
			k += 1

		while j < n2:
			a[k] = R[j]
			j += 1
			k += 1


if __name__ == "__main__":

	sortingType = "asc"

	iMerge = IterativeMergeSort()

	iMerge.mergeSort(iMerge.unsortedArray)
