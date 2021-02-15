# 정렬 되지 않은 것

arr = [4,9,11,23,9,17]

key = 23

for i in range(len(arr)):
    if key == arr[i]:
        print(i, "에 위치하고 있음")
        break

else: # break 걸려야 출력되는 문. 안걸리면 출력안됨.
    print("못찾음.")


# 정렬 되지 않은 것

arr = [4,7,9,11,23]

for i in range(len(arr)):
    if key == arr[i]:
        print(i, "에 위치하고 있음")
        break
    elif key < arr[i]:
        print(i, "번째까지만 탐색해봄")
        break
else:
    print("못찾음")