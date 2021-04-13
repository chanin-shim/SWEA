import sys
sys.stdin = open("input.txt")

T = 1

for tc in range(1,T+1):
    inp=input()
    length=7
    temp = [inp[i:i+length] for i in range(0,len(inp),length)]

    # print(temp)
#     [['0000000'], ['1111000'], ['0001100'], ['0000111'], ['1001100'], ['0011000'], ['0111100'], ['1111001'], ['1111100'], ['1100111']]

    for i in range(len(temp)):
        ans = 0
        for j in range(6,-1,-1):
            if temp[i][j] == '1':
                ans += 2**(6-j) #뒤에서 부터 오는거임 0~6의 인덱스 자리에서, 6에서 부터 -> 0까지
        print(ans)

# inp = input()
# length = 7
# tmp = [inp[i:i+length] for i in range(0, len(inp), length)]
#
# for i in range(len(tmp)):
#     ans = 0
#     for j in range(6, -1, -1):
#         if tmp[i][j] == '1':
#             ans += 2**(6-j)
#     print(ans)