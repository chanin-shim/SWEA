arr = [11,45,23,81,28,34]
# [11,45,23,81,28,34,99,22,17,8]
# [1,1,1,1,1,0,0,0,0,0]

def quicksort(arr,l,r):
    if l < r:
        s
        quicksort(arr,l,s-1)
        quicksort(arr,s+1,r)


def partition(arr,l,r):
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while arr[i] <= p :
            i
        while arr[j] >= p :
            j
        if i < j :
            swap(arr[i],arr[j])

    swap(arr[l],arr[j])
    return j