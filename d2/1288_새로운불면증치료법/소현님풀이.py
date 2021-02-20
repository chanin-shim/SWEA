import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):

    N = input()

    arr = [0 for _ in range(10)]

    # 왜 바로 int(N)으로 계산하면 안되는거지?
    intN = int(N)
    count = 1
    count_2 = count + 5
    # 아직 배열에 0이 있다면
    while 0 in arr:

        for i in N:
            if arr[int(i)] > 0:
                continue
            else:
                arr[int(i)] += 1

        count += 1
        intN = int(N)
        N = str(intN * count)

    count -= 1

    print('#{} {}'.format(tc, intN * count))




    # while문안을 계속 도는 것은 맞음 (빠져나오는 거는 아님)
    # 근데 굳이 말하자면 변수를 동일하게 지정하면 동일한 변수는 빠져나가는게 맞음.
    # 위에서 count는 바뀌어도 count2는 안바뀐다.