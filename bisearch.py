import sys

def binarySearch(alist, item):
    location = binarysearch(alist, item, 0, len(alist) - 1)
    # easier for programmer to use indicies than to manage new arrays
    return location


def binarysearch(alist, item, min, max):
    # Insert Code Here
    mid = (min+max)/2
   	
    if item == alist[mid]:
        return mid
    elif item > alist[mid]:
        return binarysearch(alist, item, mid, max)
    elif item < alist[mid]:
        return binarysearch(alist, item, min, mid)
    
    # if there is one element in the list
    if min == max:
        return -1
     
    # target is not in the list
    return -1
    
    pass


#YOU DO NOT NEED TO CHANGE THE CODE BELOW THIS LINE

#Read input
[t, n] = [int(x) for x in sys.stdin.readline().split()]
alist = [int(x) for x in sys.stdin.readline().split()]
index = binarySearch(alist, t)
print index
