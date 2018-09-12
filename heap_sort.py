import math

def LEFT(i):
    return 2 * i + 1

def RIGHT(i):
    return 2 * i + 2

def PARENT(i):
    return math.floor((i-1)/2)

def heap_size(A):
    return len(A)

def heap_length(A):
    size = len(A)
    for i in range(math.inf):
        val = math.pow(2,i) - 1
        if val == size:
            return size
        elif val > size:
            return val


# 
def max_heapify(A,i,hs):
    l = LEFT(i)
    r = RIGHT(i)
    mindex = i

    if l < hs and A[l] > A[i]:
        mindex = l
    if r < hs and A[r] > A[mindex]:
        mindex = r
    
    if i != mindex:
        A[i],A[mindex] = A[mindex],A[i]
        max_heapify(A,mindex,hs)


def build_max_heap(A,size):
    last = size - 1
    p = PARENT(last)

    for i in range(p,-1,-1):
        max_heapify(A,i,size)


def heap_sort(A):
    last = len(A)
    for size in range(last,1,-1):
        build_max_heap(A,size)
        A[size - 1],A[0] = A[0],A[size - 1]


vals = [1,3,4,2,7]
build_max_heap(vals,len(vals))
print(vals)

heap_sort(vals)
print(vals)

vals = [6,3,4,2,7,34,51,2,8,5]
build_max_heap(vals,len(vals))
print(vals)

heap_sort(vals)
print(vals)
