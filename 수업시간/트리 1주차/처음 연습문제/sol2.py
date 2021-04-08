import sys
sys.stdin = open("input.txt")

T = 1
V = int(input())
E = V-1

temp = list(map(int,input().split()))
tree = [[0 for _ in range(3)]for _ in range(V+1)]

def preorder(node):
    if node:
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])

for tc in range(1,T+1):
    # print(temp, '   ', tree)
    #[1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
    for i in range(E):
        parent, child = temp[2*i],temp[(2*i)+1]
        if not tree[parent][0]: #0이라면, 비었다면
            tree[parent][0] = child
        else :
            tree[parent][1] = child
        tree[child][2] = parent

    preorder(1)
