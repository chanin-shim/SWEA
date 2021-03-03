import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    queue = list(map(int, input().split()))
    # print(words)
    # [9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551]

    i = 0
    while True:
        i += 1 # 1~5까지 늘어날 값
        if queue[0] <= i: # 지금 첫번째 값이 뺄 값보다 작거나 같다면
            queue.pop(0)
            queue.append(0)
            break
        else: # 지금 값이 뺄값보다는 크다면
            queue.append(queue.pop(0)-i) # 그냥 빼고 맨 뒤로 가라
        if i == 5: # 5가되면 0으로 만들어서, 다음 시작할때 +1이 되도록
            i = 0

    print("#{}".format(N),end=' ')
    print(*queue,end=' ')
    print(' ')