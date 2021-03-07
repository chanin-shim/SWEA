import sys
sys.stdin = open("input.txt")

T = 10

my_num = 1
def my_square(num,square):
    if square == 1:
        return num

    return num * my_square(num,square-1)

for tc in range(1, T+1):
    N = int(input())

    number, square = map(int, input().split())



    print("#{} {}".format(tc,my_square(number,square)))