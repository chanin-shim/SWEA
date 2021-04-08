import sys
sys.stdin = open("input.txt")

T = 1

V = int(input())
E = V-1

temp = list(map(int, input().split()))
tree = [[0 for _ in range(3)]for _ in range (V+1)]


def pre_order(node):
    if node != 0:
        print('{}'.format(node), end=' ')
        pre_order(tree[node][0])
        pre_order(tree[node][1])

for tc in range(1, T+1):
    for i in range(E):
        parent, child = temp[i*2], temp[i*2+1]
        if not tree[parent][0]: #왼쪽이 비어있다면
            tree[parent][0] = child
        else:
            tree[parent][1] = child

        tree[child][2] = parent

    # 왼쪽 자식, 오른쪽 자식, 부모노드, 데이터
    # tree = [[0 for _ in range(4)]for _ in range(N+1)]

    print(pre_order(1))
    print("#{}".format(tc,))
