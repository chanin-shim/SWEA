import sys
sys.stdin = open("input.txt")

def my_reverse(line):
    r_line = []
    # 뒤에서 부터 읽어오면서 뒤집어진 리스트를 만들자!!
    for i in range(len(line)-1,-1,-1):
        r_line.append(line[i])

    return r_line

def my_find():
    #전체크기가 N
    for i in range(N):
        #가로검사
        for j in range(N-M+1):
            #부분 문자열을 위한 빈리스트
            tmp = []
            for k in range(M):
                tmp.append(words[i][j+k])

            #회문 검사
            if tmp == my_reverse(tmp):
                return tmp

        #세로검사
        for j in range(N-M+1):
            tmp = []
            for k in range(M):
                tmp.append(words[j+k][i])
            if tmp == my_reverse(tmp):
                return tmp

    #문제에서 회문이 1개 존재한다고 하였으므로 필요하지는 않음.
    return []

T = int(input())

for tc in range(1, T+1):
    # N : 2차원 리스트의 크기
    # M : 우리가 찾고 싶은 회문의 길이
    N,M = map(int, input().split())

    words = [list(input()) for _ in range(N)]


    ans = my_find()
    # print(ans)
    # ['J', 'A', 'E', 'Z', 'N', 'N', 'Z', 'E', 'A', 'J']

    print("{} {}".format(tc,''.join(ans)))