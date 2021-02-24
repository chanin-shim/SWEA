# powerset을 구하는 백트래킹 알고리즘

N = 3
arr = [1, 2, 3]  # 활용할 데이터
sel = [0] * N  # a리스트 (내가 해당원소를 뽑았는지 체크)


def powerset(idx):
    if idx == N:
        print(sel, ":", end =" ")
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')

        return

    # idx 자리의 원소를 뽑고 간다.
    sel[idx] = 1  # True
    powerset(idx + 1)
    # idx 자리를 안뽑고 간다.
    sel[idx] = 0
    powerset(idx + 1)


powerset(0)