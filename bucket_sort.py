import math


def fk(k,n):
    return math.floor(n*k)


def bucket_sort(A):
    n = len(A)
    bk = list()

    for v in A:
        bk.append(list())

    for v in A:
        f = fk(v,n)
        bk[f].append(v)

    count = 0
    for vl in bk:
        vl.sort()

        for v in vl:
            A[count] = v
            count = count + 1


vals = [1,3,4,2,7]
vals = [v/8 for v in vals]
bucket_sort(vals)
print(vals)

vals = [6,3,4,2,7,34,51,2,8,5,4,34]
vals = [v/52 for v in vals]
bucket_sort(vals)
print(vals)
