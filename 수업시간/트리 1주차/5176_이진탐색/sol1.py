import sys
sys.stdin = open("input.txt")

T = int(input())

def inorder(node):
    global cnt
    if node > 0:
        inorder(tree[node][0])
        tree[node][2] = cnt
        cnt+=1
        inorder(tree[node][1])

for tc in range(1, T+1):
    N = int(input())

    tree = [[0 for _ in range(3)]for _ in range(N+1)]
    for i in range(1, N+1):
        if 2*i < N+1:
            tree[i][0] = 2*i

        if 2*i + 1 < N+1:
            tree[i][1] = 2*i + 1

    cnt = 1
    inorder(1)
    # 왼쪽 자식, 오른쪽 자식, 데이터

    print("#{} {} {}".format(tc,tree[1][2], tree[N//2][2]))
