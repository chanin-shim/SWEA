import sys

sys.stdin = open("input.txt")

T = int(input())

def DFS(start):
    global result
    visited[start] = True
    for i in edge_list[start]:
        if not visited[i]:
            visited[i] = True
            if i == G:
                result = 1
                return
            DFS(i)


for tc in range(1, T + 1):
    V, E = list(map(int, input().split()))
    # V개의 노드(꼭짓점, vertex), E개의 간선(edge, line, 변)

    edge_list = [[]for _ in range(V+1)]
    for _ in range(E):
        start_node, end_node = list(map(int,input().split()))
        edge_list[start_node].append(end_node)

    S, G = list(map(int, input().split()))  # 1,6

    visited = [0]*(V+1)
    result = 0
    DFS(S)

    print(result)