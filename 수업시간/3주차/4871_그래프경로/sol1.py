import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    #인접행렬

    V,E = list(map(int, input().split()))
    # V개의 노드(꼭짓점, vertex), E개의 간선(edge, line, 변)

    edge_matrix = [[0 for i in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        start_node, end_node = list(map(int,input().split()))
        edge_matrix[start_node][end_node] = 1

    print(edge_matrix)

    S,G = list(map(int,input().split()))



    print("#{} ".format(tc, ))