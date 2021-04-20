import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    my_tree = [[] for _ in range(V+1)]
    for i in range(E):
        start_node, end_node = list(map(int,input().split()))
        my_tree[start_node] += [end_node]

    S,G = list(map(int,input().split()))

    print(my_tree)
    # [
    # [],
    # [4, 3],    # 1번 노드
    # [3, 5],    # 2번 노드
    # [],
    # [6],       # 4번 노드
    # [],
    # []
    # ]

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
            for v in my_tree[now]:
                #방문을 안한 노드라면
                if not visited[v]:
                    stack.append(v)

    if visited[G]:
        result = 1
    else:
        result = 0



    print("#{} {}".format(tc,result))