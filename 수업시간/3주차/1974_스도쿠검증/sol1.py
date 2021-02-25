import sys
sys.stdin = open("input.txt")

T = int(input())

N = 9

for tc in range(1, T+1):
    my_sudoku = [list(map(int,input().split())) for _ in range(N)]
    # print(my_sudoku)
    # [[7, 3, 6, 4, 2, 9, 5, 8, 1], [5, 8, 9, 1, 6, 7, 3, 2, 4], [2, 1, 4, 5, 8, 3, 6, 9, 7], [8, 4, 7, 9, 3, 6, 1, 5, 2],
    #  [1, 5, 3, 8, 4, 2, 9, 7, 6],

    result = 1

    # 행 검사
    for i in my_sudoku: # 0행,1행, 2행 ~ 8행
        check_set = set()
        for j in range(N): # 0~8
            check_set.add(i[j]) #각 행의 원소 하나하나씩 집어넣음
        if len(check_set) != N: # 중복된 값이 있으면
            result = 0 # 결과는 0이 돼라

    # 열 검사
    for i in range(len(my_sudoku)):
        check_set2 = set()
        for j in range(N):
            check_set2.add(my_sudoku[j][i])
        if len(check_set2) != N:
            result = 0

    # 우선 9*9에서 3*3으로 행으로 먼저 돌거임
    # 그리고 열 내려가서 다시 3*3으로 행 돌기
    for aa in range(0,N,3):
        for h in range(0,N,3):
            check_set3 = set()
            for i in range(3): #0 1 2
                for j in range(3):
                    check_set3.add(my_sudoku[i+h][j+aa])
            if len(check_set3) != 9:
                result = 0


    print("#{} {}".format(tc,result))