import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N,M,L = input().split()
    N = int(N)
    M = int(M)
    L = int(L)
    # N = 노드개수
    # M = 리프 노드 개수
    # L = 출력할 노드 번호
    tree = [[0 for _ in range(4)] for _ in range(N+1)]
    # 데이터, 왼자, 오자, 부모

    for i in range(M):
        leafnode_num, data = input().split()
        leafnode_num = int(leafnode_num)
        data = int(data)
        tree[leafnode_num][0] = data

    # print(tree)
    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [3, 0, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0]]

    for i in range(M,0,-1):
        if tree[i][0] == 0:
            if i*2 <= N:
                tree[i][0] = tree[i*2][0]
                if i *2 +1 <= N:
                    tree[i][0] += tree[i*2+1][0]


    print("#{} {}".format(tc,tree[L][0]))