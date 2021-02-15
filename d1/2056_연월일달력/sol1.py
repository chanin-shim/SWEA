import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    date = input()
    year = date[0:4]
    month = date[4:6]
    day = date[6:9]
    # 날짜 설정

    ans = 0
    if int(year) <= 0 or int(month) <= 0 or int(day) <= 0  \
            or (int(day) > 31) \
            or (int(month) == 2 and int(day) > 28) or(int(month) == 4 and int(day) >30) or (int(month) == 9 and int(day) >30) or (int(month) == 11 and int(day) >30):
        ans = -1
    else:
        ans = year+"/"+month+"/"+day


    print("#{} {}".format(tc,ans))

