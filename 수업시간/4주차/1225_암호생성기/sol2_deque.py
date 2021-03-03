from collections import deque

import sys
sys.stdin = open("input.txt")

T = 10

for tc in range(1, T+1):
    N = int(input())
    my_deque = deque(list(map(int, input().split())))
    # print(my_deque)
    # deque([9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551])

    i = 0
    while True:
        i+=1
        if my_deque[0] <= i:
            my_deque.popleft()
            my_deque.append(0)
            break
        else:
            my_deque.append(my_deque.popleft()-i)
        if i == 5:
            i = 0

    # print(*my_deque)
    # 6 2 2 9 4 1 3 0


    print("#{}".format(tc),end=' ')
    print(*my_deque)

