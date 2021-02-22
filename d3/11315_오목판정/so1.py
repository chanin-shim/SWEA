import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # N = 판의 크기. N*N

    my_list = []
    for i in range(N):
        my_list += [str(input())]
    # ['....o',
    #  '...o.',
    #  '..o..',
    #  '.o...',
    #  'o....']

    ans = 'NO'

    for i in range(N):
        cnt = 0
        for j in range(N):
        # 가로 연속하다면
            if my_list[i][j] == 'o':
                cnt+=1
                if cnt == 5:
                    ans = 'YES'
            else:
                cnt = 0

    for i in range(N):
        cnt_2 = 0
        # 세로 연속하다면
        for j in range(N):
            if my_list[j][i] == 'o':
                cnt_2+=1
                if cnt_2 == 5:
                    ans = 'YES'
            else:
                cnt_2 = 0

    cnt_diag = 0
    for i in range(N):
    # 우 하향 대각선 연속하다면
        for j in range(N):
            if my_list[i][j] == 'o':
                cnt_diag += 1
                if cnt_diag == 5:
                    ans = 'YES'
                if i+1 or j+1 > N-1:
                    continue
                else:
                    if my_list[i+1][j+1] != 'o':
                        cnt_diag = 0

    cnt_diag2 = 0
    for i in range(N):
        for j in range(N-1,-1,-1):
        # 좌 하향 대각선 연속하다면
            if my_list[i][j] == 'o':
                cnt_diag2 += 1
                if cnt_diag2 == 5:
                    ans = 'YES'
                if i+1 > N-1 or j-1 < 0:
                    continue
                else:
                    if my_list[i+1][j-1] != 'o':
                        cnt_diag2 = 0

    print("#{} {}".format(tc,ans))


# 10*10이 있다면, 모서리를 잇는 큰 대각선만 있는게 아니라
# 작은 대각선으로도 5를 충분히 이을 수 있음.