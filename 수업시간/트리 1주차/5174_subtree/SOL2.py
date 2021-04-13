import sys
sys.stdin = open("input.txt")

T = int(input())

def size(node):
    global cnt
    if not tree[node][0]:
        return
    else:
        if tree[node][0]:
            cnt+=1
            size[tree[node][0]]
        if tree[node][1]:
            cnt+=1
            size([tree][node][1])

tree =

for tc in range (T+1):
    E, N = input().split()
    temp = list(map(int,input().split()))
    for i in range(E):
        parent = temp[i*2]
        child = temp[i*2+1]
