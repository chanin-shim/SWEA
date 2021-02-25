numbers = [3,9,4,7,5,0,1,2,6,8]

def partition(arr, start, end):
    pivot = arr[start] # arr을 numbers라고 생각해도됨
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and arr[left] <= pivot: # left가 먼저 출발하므로, left는 right보다 작거나 같아야함.
            left += 1
        while left <= right and arr[right] >= pivot  :
            right -= 1 # 왼쪽으로 하나씩 이동해야 해서.

        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start] # 다 끝나고, 스타트랑 라이트랑 값을 바꿔줌.
    return right # 바꿔서 지금 right에 피벗이 저장되어 있음.

    # L이랑 R이 스왑되는 순간이, 가운데를 기준으로 작은것들, 큰것들 나뉜거임
    # 그리고 numbers[0]과 R의 자리를 바꿈.


def quick_sort2(arr,start,end):
    if start < end:
        pivot = partition(arr, start, end)
        # 근데 이거 파티션 돌리면 right(실제로는 pivot)이 나옴.
        quick_sort2(arr,start,pivot-1) # 피봇을 기준으로 왼쪽 퀵 솔트를 돌림
        quick_sort2(arr, pivot+1, end)
    return arr

print(numbers)
print(quick_sort2(numbers, 0, len(numbers)-1))
