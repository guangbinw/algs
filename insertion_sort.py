
def insertion_sort(array):
    li = len(array)
    if li <= 1:
        return array
    
    for i in range(1,li):
        key = array[i]

        j = i - 1
        while j >= 0 and key > array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j+1] = key

    return array

vals = [1,3,4,2,7]
print(insertion_sort(vals))

vals = [6,3,4,2,7]
print(insertion_sort(vals))
