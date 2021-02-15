arr = [10,15,2,19,6,14]

for i in range(len(arr)-1):
    min_idx = i
    # i = 0 ~4

    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_idx]: # 내가 현재 보고있는값이, 내가 가지고있는 최소값보다 작아?
            min_idx = j #그러면 min_idx 갱신
            # 갱신은 몇 번 이든 일어날 수 있고

    arr[i], arr[min_idx] = arr[min_idx],arr[i]
        #교환만 마지막에 제대로 한다.

        # tmp = arr[i]
        # arr[i] = arr[min_idx]
        # arr[min_idx] = tmp
        # 이 방법도 인지하고 있어야함

    print("기준자리:",i,arr)

        # 첫번째 사이클이 끝나면 [2,15,10,19,6,14]가 됨.

print(arr)