import sys
sys.stdin = open("input.txt")

T = int(input())

# 1) 월별 날짜 담은 dict 생성
# 2) 날짜 계산은 쉬움
# 3) 월 계산은 월들을 range에 넣고, 각 첫째월과 마지막월 사이의 해당하는 전체 날짜값을 다 더해줌
# 4) but 마지막 날짜 월은 넣지 않음 **
# 5) 그리고 첫째 월의 날짜값은 빼주고 마지막 월의 날짜값은 더해줌 **
# 4), 5)를 이해하는게 오래걸렸음

month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

for tc in range(1, T+1):
    month1, day1, month2, day2 = map(int, input().split())
    # print(month1, day1, month2, day2)
    # 3 1 3 31

    month_minus = month2 - month1
    month_term = 0

    if month_minus == 0:
        ans = day2 - day1 + 1

    else:
        for i in range(month1, month2):
            month_term += month_dict[i]
            ans = month_term -day1 +day2 + 1
            # 솔직히 1 왜 더해야하는지 아직 잘 이해 안갔음.


    print("#{} {}".format(tc,ans))