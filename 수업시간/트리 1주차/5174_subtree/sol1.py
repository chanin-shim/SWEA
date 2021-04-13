import sys
sys.stdin = open("input.txt")

T = int(input())

def size(node):
    global cnt
    if not tree[node][0] :
        return
    else:
        if tree[node][0]:
            cnt += 1
            size(tree[node][0])
        if tree[node][1]:
            cnt += 1
            size(tree[node][1])


for tc in range(1, T+1):
    E, N = map(int, (input().split()))
    tree = [[0 for _ in range(3)]for _ in range(E*2+1)]
    # 왼자, 오자, 부모
    V = E+1
    temp = list(map(int,input().split()))
    for i in range(E):
        parent, child = temp[i*2], temp[i*2+1]
        if tree[parent][0] == 0: # 왼자 비어있따면
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent

    cnt = 1
    size(N)
    print(cnt)



    print("#{} ".format(tc, ))