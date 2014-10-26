def binarySearch(a, x):
    ''' takes in a sorted list x and a value to look for a '''
    #another basecase. also defensive
    if x == []:
        return False

    z = len(x)/ 2
    #major basecase
    if x[z] == a:
        return True

    elif x[z] > a:
        if binarySearch(a, x[:z-1]):
            return True
        else:
            return False
    elif x[z] < a:
        if binarySearch(a, x[z+1:]):
            return True
        else:
            return False

def test():
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print binarySearch(6, mylist)
    print binarySearch(4, mylist)
    print binarySearch(21, mylist)
    print binarySearch(1, mylist)
    print binarySearch(0, mylist)
    print binarySearch('x', mylist)
    print binarySearch(20, mylist)
    print binarySearch('20', mylist)

def testFile(fileName='IntegerArray.txt'):
    dataFile = open(fileName, "r")
    intArray = [int(line) for line in dataFile]
    #array has to be sorted! use inbuilt python sorted 
    intArray = sorted(intArray)

    print binarySearch(1, intArray)
    print binarySearch(100000, intArray)
    print binarySearch(0, intArray)
    print binarySearch(100001, intArray)
    print binarySearch(50000, intArray)
    print binarySearch(-10, intArray)

def testString():
    stringList = ['ahmed', 'hekmat', 'hello', 'mona', 'moody', 'world']
    print binarySearch('ahmed', stringList)
    print binarySearch('world', stringList)
    print binarySearch('mona', stringList)
    print binarySearch('hekmat', stringList)
    print binarySearch('moody', stringList)
    print binarySearch('hello', stringList)
    print binarySearch('bilal', stringList)
    print binarySearch(20, stringList)

