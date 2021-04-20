import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    V, E = list(map(int, input().split()))
    # V개의 노드(꼭짓점, vertex), E개의 간선(edge, line, 변)

    edge_list = [[]for _ in range(V+1)]
    for _ in range(E):
        start_node, end_node = list(map(int,input().split()))
        edge_list[start_node].append(end_node)

    S, G = list(map(int, input().split()))  # 1,6

    visited = [0]*(V+1)
    queue = [S]

    while queue:
        now = queue.pop(0)
        # 방문한 경우
        if not visited[now]:
            visited[now] = True
            #현재 노드와 연결된 모든 노드를 반복
            for v in edge_list[now]:
                if not visited[v]:
                    queue.append(v)
    result = 1 if visited[G] else 0

    print(edge_list)