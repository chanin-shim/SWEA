import sys
sys.stdin = open("input.txt")

T = int(input())

def search_size(r,c):
    r_cnt = 0
    c_cnt = 0

    # 행의 길이를 찾는
    for i in range(r,N):
        if arr[i][c] != 0:
            r_cnt += 1
        else:
            break
    # 열의 길이를 찾는
    for i in range(c, N):
        if arr[r][i] != 0:
            c_cnt=1
        else:
            break

    ans.append([r_cnt,c_cnt,r_cnt*c_cnt])

# 화학물질들을 빈 용기로 전환 = 초기화 하는 작업
def init(r,c,r_cnt,c_cnt):
    for i in range(r, r+r_cnt):
        for j in range(c,c+c_cnt):
            arr[i][j] = 0

    # 카운팅 정렬
def counting_sort(idx):
    cnt = [0] * 10001
    sort_ans = [0] * len(ans)

    # 1. 카운팅 하는 과정
    for i in range(len(ans)):
        cnt[ans[i][idx]] += 1

    #




for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = []

    # 행 우선순회 방식으로 순회하면서 사각형의 시작좌표를 구한다.
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                search_size(i,j)