import sys
sys.stdin = open("input.txt")

T = 10

def in_order(node):
    if tree[node][3] != 0:
        in_order(tree[node][0])
        print(tree[node][3], end='')
        in_order(tree[node][1])

for tc in range(1, T+1):
    N = int(input())

    # 왼쪽 자식, 오른쪽 자식, 부모노드, 데이터
    tree = [[0 for _ in range(4)]for _ in range(N+1)]

    for i in range(N):
        # 1 W 2 3 / 8 S
        node_info = list(input().split())
        node_num = int(node_info[0])
        node_data = node_info[1]
        # lc = node_info[2]
        # rc = node_info[3]

        tree[node_num][3] = node_data
        if node_num * 2 <= N:
            tree[node_num][0] = int(node_info[2])
            if node_num * 2 + 1 <= N:
                tree[node_num][1] = int(node_info[3])
