import sys
sys.stdin = open("input.txt")

T = 10

V = int(input())
E = V-1
tree = [[0 for _ in range(3)]for _ in range (V+1)]

for tc in range(1, T+1):
    N = int(input())

    # 왼쪽 자식, 오른쪽 자식, 부모노드, 데이터
    tree = [[0 for _ in range(4)]for _ in range(N+1)]


    print("#{}".format(tc, ))