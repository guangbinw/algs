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
def max_heapify(A,i):
    l = LEFT(i)
    r = RIGHT(i)
    mindex = i

    if l < heap_size(A) and A[l] > A[i]:
        mindex = l
    if r < heap_size(A) and A[r] > A[mindex]:
        mindex = r
    
    if i != mindex:
        A[i],A[mindex] = A[mindex],A[i]
        max_heapify(A,mindex)


def build_max_heap(A):
    last = len(A) - 1
    p = PARENT(last)

    for i in range(p,-1,-1):
        max_heapify(A,i)


def heap_sort(A):
    last = len(A) - 1
    for size in range(last):
        build_max_heap(A[:last-size+1])
        A[last-size],A[0] = A[0],A[last-size]

vals = [1,3,4,2,7]
build_max_heap(vals)
print(vals)

heap_sort(vals)
print(vals)

vals = [6,3,4,2,7,34,51,2,8,5]
build_max_heap(vals)
print(vals)

heap_sort(vals)
print(vals)
