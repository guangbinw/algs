import math


def fk(k,m,n):
    return math.floor(n*k/m)


def bucket_sort(A,m):
    n = len(A)
    bk = list()

    for v in A:
        bk.append(list())

    for v in A:
        f = fk(v,m,n)
        bk[f].append(v)

    count = 0
    for vl in bk:
        vl.sort()

        for v in vl:
            A[count] = v
            count = count + 1


vals = [1,3,4,2,7]
bucket_sort(vals,8)
print(vals)

vals = [6,3,4,2,7,34,51,2,8,5,4,34]
bucket_sort(vals,52)
print(vals)
