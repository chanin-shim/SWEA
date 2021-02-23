arr = [int(x) for x in input()]

cnt = 0
if arr[0] == 1:
    cnt = 1

for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        cnt += 1

print('#{} {}'.format(tc, cnt))