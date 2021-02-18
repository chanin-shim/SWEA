import sys
sys.stdin = open("input.txt")

T = int(input())

def bisearch(end,key):
    start = 1
    end = 0
    while True:
        middle =

def bisearch(end,key):
    start = 1
    cnt = 0
    while start <= end :
        middle = int((start+end)/2)
        cnt += 1
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
        elif middle < key:
            start = middle

for tc in range(1, T+1):
    end, a_paper, b_paper = map(int, input().split())
    # print(total_paper, a_paper, b_paper)
    # 400 300 350
    # 1000 299 578
    # 1000 222 888

    #print(bisearch(end,a_paper))
    # 2, 9, 10

    if bisearch(end, a_paper) > bisearch(end, b_paper):
        result = 'B'
        # cnt 값이 a가 더 크니까, b가 더 적게 돌았다는 것이므로, B승리!

    elif bisearch(end, a_paper) < bisearch(end, b_paper):
        result = 'A'
        # cnt 값이 b가 더 크니까, a가 더 적게 돌았다는 것이므로, A승리!

    else:
        result = '0'
        # 겹치면 0

    print('#{} {}'.format(tc,result))