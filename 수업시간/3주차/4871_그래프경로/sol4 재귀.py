import sys
sys.stdin = open("input.txt")

T = int(input())

def DFS(start):
    global result
    visited[start] = True # 방문했다고 한거임
    for node in edge_list[start]:
        # 방문 안했다면 방문하기
        if not visited[node]:
            if node == G: #도착지와 같다면
                result = 1
                return
            DFS(node)


for tc in range(1, T+1):
    V,E = list(map(int, input().split()))
    # V개의 노드(꼭짓점, vertex), E개의 간선(edge, line, 변)

    edge_list = [[] for _ in range(V+1)]

    for _ in range(E):
        start_node, end_node = list(map(int, input().split()))
        edge_list[start_node].append(end_node)

    S,G = list(map(int, input().split()))

    visited = [False] * (V+1) # 일단 FALSE로 두고, 방문할때마다 True로 바꿔줌
    result = 0
    DFS(S)


    print("#{} {}".format(tc,result))