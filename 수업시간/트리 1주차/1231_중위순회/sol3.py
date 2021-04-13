import sys
sys.stdin = open("input.txt")

T = 10

def order(node):
    if node != 0:
        order(tree[node][1])
        print(tree[node][3], end=' ')
        order(tree[node][2])

for tc in range(1,T+1):
    N = int(input())
    tree = [[0 for _ in range(4)] for _ in range(N + 1)]
    # 부모,왼자,오자,데이터
    for i in range (N):
        temp = list(input().split())
        # 현재 노드, 데이터, 왼자,오자
        node_num = int(temp[0])
        node_data = temp[1]
        if len(temp) == 4:
            child1 = int(temp[2])
            child2 = int(temp[3])
            tree[node_num][1]=child1
            tree[node_num][2]=child2
            tree[node_num][3]=node_data
            tree[child1][0]=tree[node_num]
            tree[child2][0]=tree[node_num]
        elif len(temp) == 3:
            child1 = int(temp[2])
            tree[node_num][1] = child1
            tree[node_num][3] = node_data
            tree[child1][0] = tree[node_num]
        elif len(temp) == 2:
            tree[node_num][3] = node_data


    order(1)
    print()
