import sys
sys.stdin = open("input.txt")

T = int(input())

goal_set = {0,1,2,3,4,5,6,7,8,9}

for tc in range(1, T+1):
    my_set = set()
    # my_set.add('i')
    # print(my_set)
    # {'i'}

    N = int(input())
    count = 0
    ans = 0
    temp = 0
    while True:
        count += 1
        present_N = N * count
        for i in range(len(str(present_N))):
            my_set.add(int(str(present_N)[i]))
            if my_set == goal_set:
                ans = present_N
                temp = -999
        if temp == -999:
            break

        # 전기버스랑 같은 문제
        # while 문안의 for 문안의 if문에서 빠져나오는 방법 알아야함.


    print("#{} {}".format(tc, ans))







import sys
sys.stdin = open("input.txt")
​
T = int(input())
​
for tc in range(1, T + 1):
​
    N = input()
​
    arr = [0 for _ in range(10)]
​
    # 왜 바로 int(N)으로 계산하면 안되는거지?
    intN = int(N)
    count = 1
​
    # 아직 배열에 0이 있다면
    while 0 in arr:
​
        for i in N:
            if arr[int(i)] > 0:
                continue
            else:
                arr[int(i)] += 1
​
        count += 1
​
        N = str(intN * count)
​
    count -= 1
​
    print('#{} {}'.format(tc, intN * count))



