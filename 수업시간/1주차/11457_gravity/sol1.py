import sys
sys.stdin = open("input.txt")

T = list(map(int,input().split()))
print(T)

def gravity(numbers) :
    #가장 긴 상자를 찾기
    longlong = 0
    for idx in numbers:
        if numbers[idx] > numbers[idx+1] :
            numbers[idx+1] = numbers[idx]
            longlong = numbers[len(numbers)]
    for idx in numbers:
        if numbers.count(longlong) >=2:

        else:
            longlong -


#
# for tc in range(1, T+1):
#
#     print("#{} ".format(tc, ))

