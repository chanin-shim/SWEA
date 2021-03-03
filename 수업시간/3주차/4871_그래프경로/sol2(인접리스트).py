import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):

    # 인접리스트

    V, E = list(map(int, input().split()))
    # V개의 노드(꼭짓점, vertex), E개의 간선(edge, line, 변)

    edge_list = [[]for _ in range(V+1)]
    for _ in range(E):
        start_node, end_node = list(map(int,input().split()))
        edge_list[start_node].append(end_node)

    print(edge_list)
    # [[], [4, 3], [3, 5], [], [6], [], []]

    S, G = list(map(int, input().split())) #1,6

    visited = [0] * (V+1)
    # [0, 0, 0, 0, 0, 0, 0]
    stack = [S]

    while stack: # 하나라도 스택에 있다면 반복해라
        now = stack.pop()
        # 방문한경우
        if visited[now]: #0이면 방문을 안했다는 거고, 1이면 방문을 했다는 거임
            pass
        #방문하지 않은경우
        else:
            visited[now] = True
            # 현재(now) 노드와 연결된 모든 노드를 반복
            for v in edge_list[now]:
                #방문을 안한 노드라면
                if not visited[v]:
                    stack.append(v)

    result = 1 if visited[G] else 0



    print("#{} {}".format(tc,ans))