import math

#r = last_index
def partion(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r): # j = [p,r-1]
        if A[j] <= x:
            i = i+1
            if i != j:
                A[j],A[i] = A[i],A[j]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1


def quick_sort(A,p,r):
    if p < r:
        q = partion(A,p,r)
        print(p,r,q,'',A)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)



vals = [1,3,4,2,7]
quick_sort(vals,0,len(vals)-1)
print(vals)


vals = [6,3,4,2,7,34,51,2,8,5]
quick_sort(vals,0,len(vals)-1)
print(vals)
