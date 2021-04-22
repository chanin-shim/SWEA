import sys

sys.stdin = open("input.txt")

def DFS(start):
    visited[start] = True
    for node in my_tree[start]:
        if visited[node] != True:
            DFS(node)


T = int(input())
for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    my_tree = [[] for _ in range(V+1)]
    for i in range(E):
        start_node, end_node = list(map(int,input().split()))
        my_tree[start_node] += [end_node]

    S,G = list(map(int,input().split()))

    visited = [0] *(V+1)
    DFS(S)

    print("#{} {}".format(tc,result))