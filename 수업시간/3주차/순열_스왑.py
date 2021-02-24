arr = [1,2,3]

N = 3

def perm(idx):
    if idx == N:
        print(arr)

    else:
        for i in range(idx,N):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx + 1)
            #원상복귀
            arr[idx], arr[i] = arr[i], arr[idx]


