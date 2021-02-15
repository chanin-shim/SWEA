import sys
sys.stdin = open("input.txt")

T = input()
my_list = []
for i in range(0,len(T)):
    if len(T) < 6:
        result = 1
    else:
        my_list += int(T[i])
        total = {}
        for j in my_list:
            total += j
            if len(total) <= 2:
                result = 1
            else:
                result = 0
# 이건 나중에 절반은 run이고 절반은 triple 일때를 못잡음.

#my_list = [0,5,4,0,6,0]

print(result)
