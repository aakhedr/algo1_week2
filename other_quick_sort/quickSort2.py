def quickSort(A):
   quickSortHelper(A, len(A))

def quickSortHelper(A, n):
   if n < 2:
      return
   else:
      first, last = 0, n - 1
      pivot_index = partition(A, first, last)
      quickSortHelper(A, len(A[first:pivot_index - 1]))
      quickSortHelper(A, len(A[pivot_index + 1: last]))

def partition(A, left, right):
   pivot = A[left]
   i, j = left + 1, left + 1
   while j <= right:
      if A[j] < pivot:
         A[j], A[i] = A[i], A[j]
         i += 1
      j += 1
   A[left], A[i - 1] = A[i -1], A[left]
   return i - 1

def testFile(dataFile='10.txt'):
   #QuickSort.txt              10,000 ints
   #10.txt
   #100.txt
   #1000.txt
   inFile = open(dataFile, "r")
   intArray = [int(line) for line in inFile]
   quickSort(intArray)
   return len(intArray), intArray[0], intArray[len(intArray) - 1]
