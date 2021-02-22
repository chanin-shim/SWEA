import sys
sys.stdin = open("input.txt")

T = 10

for _ in range(1, T+1):
    tc = int(input())
    N = 100 # 100 X 100 의 문자의 행렬
    matrix = [] # 가로방향으로 문자들을 가지고 와서 리스트에 저장
    colmatrix = [] # 세로방향으로 문자들을 가지고 와서 리스트에 저장
    for i in range(N):
        matrix.append(input())
    print(matrix)
