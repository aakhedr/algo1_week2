def quickSort(A):
    quickSortHelper(A, 0, len(A) - 1)

def quickSortHelper(A, first, last):
    if first < last:
        pivot_index = partition(A, first, last)
        
        quickSortHelper(A, first, pivot_index - 1)
        quickSortHelper(A, pivot_index + 1, last)

def partition(A, first, last):
    '''
    The partition around the pivot element part -
    Pivot is chosen according to MEDIAN OF THREE pivot rule
    '''
    print 'A before partition', A
    print 'first', first, 'last', last

    # choose a MEDIAN OF THREE pivot element from the array passed
    if (last - first + 1) % 2 == 0:
        mid = ((last - first + 1) / 2) - 1 + first
    else:
        mid = ((last - first)/ 2 + first) 
    three = sorted([A[first], A[mid], A[last]])

    # pick the median of three
    median = three[1]

    ## swap the median with the first element of the aray
    if median == A[mid]:
        A[first], A[mid] = A[mid], A[first]
    elif median == A[last]:
        A[first], A[last]  = A[last], A[first]

    pivot = A[first]
    i, j = first + 1, first + 1
    while j <= last:
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
        j += 1
    A[first], A[i - 1] = A[i -1], A[first]
    return i - 1
