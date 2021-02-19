import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    N, M = map(int, input().split())
    # print(N, M)
    # 5 3
    my_list = []

    for i in range (N):
        my_list += [list(map(int,input().split()))]

    #가로 확인
    for i in range(len(my_list)): #0~4
        cnt = 0
        for j in range(N): # 0~2
            if my_list[i][j] == 1:
                cnt += 1

            if my_list[i][j] or j == N -1:
                #벽을 만났을 때 그동안 쌓아온 cnt값이 K이면 들어갈 수 있다.
                if cnt == K:
                    ans += 1
                cnt = 0
        #열을 검사
        for j in range(N):
            if my_list[j][i] == 1:
                cnt += 1
            if my_list[j][i] == 0 or j == N -1:
                if cnt = K:
                    ans += 1
                cnt = 0

#########################################################################


    puzzle = [list(map(int, input().split())) +[0] for _ in range(N)]
    puzzle.append([0]*(N+1))

    ans = 0

    for i in range(N):
        cnt = 0
        #벽을 한칸 더 둘렀기 때문에 증가
        for j in range(N+1):
            if puzzle[i][j]:
                cnt+=1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
        for j in range(N+1):
            if puzzle[j][i]:
                cnt+=1
            else:
                if cnt == K:
                    ans+=1
                    cnt=0

    print()

    print(my_list)

    print("#{} ".format(tc, ))