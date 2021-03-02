import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(start,end):
    stack = []
    visit = [False] * V


for i in range(1,T+1):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visit = [True for _ in range(V+1)]