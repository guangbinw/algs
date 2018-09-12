import math


def bubble_sort(A):
    for i in range(len(A)):
        s_range = range(len(A)-1,i,-1)
        for j in s_range:
            if A[j-1] < A[j]:
                A[j-1],A[j] = A[j],A[j-1]


vals = [1,3,4,2,7]
bubble_sort(vals)
print(vals)

vals = [6,3,4,2,7,34,51,2,8,5]
bubble_sort(vals)
print(vals)
