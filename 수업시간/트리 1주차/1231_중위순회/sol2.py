import sys
sys.stdin = open("input.txt")

T = 10

def in_order(node):
    if node != 0:
        in_order(tree[node][0])
        print(tree[node][3], end='')
        in_order(tree[node][1])

for tc in range(1,T+1):
    N = int(input())
    tree = [[0 for _ in range (4)]for _ in range(N+1)]

    for i in range(N):
        # 내가 원하는 것
        # [자식1, 자식2, 부모, 데이터]

        # print(node_info)
        # ['1', 'W', '2', '3']
        # ['2', 'F', '4', '5']
        # ['3', 'R', '6', '7']

        node_info = input().split()
        node_num = int(node_info[0])
        node_data = node_info[1]
        if len(node_info) > 2:
            if len(node_info) == 3:
                lc = int(node_info[2])
                # 자식 노드 넣어주기
                tree[node_num][0] = lc
                # 부모 노드 넣어주기
                tree[lc][2] = node_num
                # 데이터 넣어주기
                tree[node_num][3] = node_data
            else:
                lc = int(node_info[2])
                rc = int(node_info[3])
                # 자식 노드 넣어주기
                tree[node_num][0] = lc
                tree[node_num][1] = rc
                # 부모 노드 넣어주기
                tree[lc][2] = node_num
                tree[rc][2] = node_num
                # 데이터 넣어주기
                tree[node_num][3] = node_data
        else :
            # 데이터 넣어주기
            tree[node_num][3] = node_data

    print("#{}".format(tc), end=' ')
    in_order(1)
    print()