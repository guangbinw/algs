import math


def counting_sort(A,B,k):
    #counting
    C = [0] * k

    '''
    C-style code
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1
    '''
    for v in A:
        C[v] = C[v] + 1
    
    for i in range(1,k):
        C[i] = C[i] + C[i-1]
    
    for v in A:
        c_index = C[v] - 1 # first index = 0, not 1
        B[c_index] = v
        C[v] = C[v] - 1


vals = [1,3,4,2,7]
result = [0] * len(vals)
counting_sort(vals,result,8)
print(result)


vals = [6,3,4,2,7,34,51,2,8,5,4,34]
result = [0] * len(vals)
counting_sort(vals,result,52)
print(result)
