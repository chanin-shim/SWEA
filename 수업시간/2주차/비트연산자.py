# 비트 연산자

# & = and 연산
# | = or 연산
# << = 피연산자의 비트 열을 왼쪽으로 이동시킨다.
# >> = 오른쪽으로
# if 이동시킨다:

# ex)
# 0110 -> 6
# 1011 -> 11
# (&연산시)
# -> 0010 ->2
# (|연산시)
# -> 1111 -> 15

print(6&11)
print(6|11)

#######################

# <<연산자

# 1<<n : 2^n 즉, 원소가 n개일 경우 모든 부분집합의 수를 의미한다.
# for i in range(1<<n):
#     for j in range(n):
#         if i & (i<<j):



ingredient = ["계란", "치즈", "떡"]

N = 3

for i in range(1<<N):
# (0~8까지 도는거)
    ans = ""
    for j in range(N):
        if i & (1<<j):
            ans+= ingredient[j] + " "

    print(ans, "라면입니다.")

 라면입니다.  -> 0   000
계란  라면입니다. --> 1    001
치즈  라면입니다. --> 2    010
계란 치즈  라면입니다. -->3
떡  라면입니다. --> 4
계란 떡  라면입니다. --> 5
치즈 떡  라면입니다. --> 6
계란 치즈 떡  라면입니다. --> 7    111
