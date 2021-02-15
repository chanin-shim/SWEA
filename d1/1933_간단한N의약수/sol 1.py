import sys
sys.stdin = open("input.txt")

num = int(input())


for i in range(1,num+1):
    if num % i == 0 :
        print(i, end=" ")
