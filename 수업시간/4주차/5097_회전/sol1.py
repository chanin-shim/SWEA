import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    queue = list(map(int,input().split()))
    # print(queue)
    # [5527, 731, 31274]

    cnt=0

    while cnt!=M:
        cnt+=1
        queue.append(queue.pop(0))

    ans = queue[0]


    print("#{} {}".format(tc,ans))