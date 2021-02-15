import sys
sys.stdin = open("input.txt")

num = list(map(int,input().split()))
#가위는 1, 바위는 2, 보는 3

# num[0]이 A, num[1]가 B


if num[0] == 1:
    if num[1] == 2:
        print("B")
    if num[1] == 3:
        print("A")

if num[0] == 2:
    if num[1] == 1:
        print("A")
    if num[1] == 3:
        print("B")

if num[0] == 3:
    if num[1] == 1:
        print("B")
    if num[1] == 2:
        print("A")