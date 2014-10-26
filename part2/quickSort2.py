def quickSort(A, fileName):
    quickSortHelper(A, 0, len(A) - 1, fileName)

def quickSortHelper(A, first, last, fileName):
    if first < last:
        pivot_index = partition(A, first, last, fileName)
        
        quickSortHelper(A, first, pivot_index - 1, fileName)
        quickSortHelper(A, pivot_index + 1, last, fileName)

def partition(A, first, last, fileName):
    '''
    The partition around the pivot element part - Pivot is always the LAST element of the array

    fileName parameter refers to the file that will be written to calculate the comparisons
    and the number of paritions 
    '''
    ### File writing part ### Not related to the algorith 
    f = open("count_" + fileName, "a")
    f.write(str(last - first) + '\n')
    f.close()
    ###

    ### swap pivot (last element) with the first element
    A[first], A[last] = A[last], A[first]

    pivot = A[first]
    i, j = first + 1, first + 1
    while j <= last:
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
        j += 1
    A[first], A[i - 1] = A[i -1], A[first]
    return i - 1

import os 

def count(dataFile):
    inFile = open(dataFile, "r")
    total = [int(line) for line in inFile]
    comparisons, partitions = sum(total), len(total)
    os.remove(dataFile)
    return comparisons, partitions

def sort():
    '''
    Computes the number of comparisons and the number of partitions
    (i.e. recurisve calls) in quickSort algorithm when using the first element
    of the array as the pivot.
    '''
    files= ['10.txt', '100.txt', '1000.txt', '10000.txt']
    result = []

    for aFile in files:
        inFile = open(aFile, "r")
        intArray = [int(line) for line in inFile]
        quickSort(intArray, aFile)
        comparisons, partitions = count("count_" + aFile)
        result.append((comparisons, partitions))
    return result

print sort()
# import timeit

# t = timeit.Timer(sort)
# print 'pivot last', t.timeit(number=1)
