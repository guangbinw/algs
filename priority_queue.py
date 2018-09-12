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


def insert(S,key):
    x = len(S)
    S.append(-1)
    increase_key(S,x,key)


def maximum(S):
    if len(S) > 0:
        return S[0]
    return math.inf

def extract_max(S):
    l_index = len(S) - 1
    val = S[0]

    S[0],S[l_index] = S[l_index],S[0]
    S.pop(l_index)

    max_heapify(S,0,len(S))
    return val


def increase_key(S,x,key):
    ki = x
    if S[ki] > key:
        return 
    S[ki] = key
    
    while ki > 0:
        pi = PARENT(ki)
        if S[ki] > S[pi]:
            S[pi],S[ki] = S[ki],S[pi]
            ki = pi
        else:
            break


vals = [1,3,4,2,7]
build_max_heap(vals,len(vals))
print(vals)

vals = []
insert(vals,1)
insert(vals,3)
insert(vals,4)
insert(vals,2)
insert(vals,7)

print(extract_max(vals))
print(extract_max(vals))
print(extract_max(vals))
print(extract_max(vals))
print(extract_max(vals))


heap_sort(vals)
print(vals)

vals = [6,3,4,2,7,34,51,2,8,5]
build_max_heap(vals,len(vals))
print(vals)

heap_sort(vals)
print(vals)
