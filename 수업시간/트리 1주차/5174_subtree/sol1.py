import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    E, N = map(int, (input().split()))
    tree = [[0 for _ in range(2)]for _ in range(E*2+1)]

    V = E+1
    temp = list(map(int,input().split()))
    for i in range(E):
        parent, child = temp[i*2], temp[i*2+1]

    # 자식, 부모
    tree[parent][0] = child
    tree[child][1] = parent


    print("#{} ".format(tc, ))