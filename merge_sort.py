import math

MAX_VAL = math.inf

def merge(A,p,q,r):
    L = list(A[p:q+1])
    R = list(A[q+1:r+1])

    L.append(MAX_VAL)
    R.append(MAX_VAL)

    li = 0
    ri = 0

    for i in range(p,r + 1):
        if L[li] < R[ri]:
            A[i] = L[li]
            li += 1
        elif L[li] != MAX_VAL:
            A[i] = R[ri]
            ri += 1


def merge_sort(A,p,r):
    if p < r:
        q = math.floor((p+r)/2)
        print(p,q,r)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)


vals = [1,3,4,2,7]
merge_sort(vals,0,4)
print(vals)

vals = [6,3,4,2,7,34,51,2,8,5]
merge_sort(vals,0,9)
print(vals)
