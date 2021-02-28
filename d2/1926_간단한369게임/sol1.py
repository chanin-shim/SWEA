import sys
sys.stdin = open("input.txt")

N = int(input())

my_list = []
for i in range(N):
    my_list += [str(i)]

for i in my_list:
    print(i[len(i):0:-1])


    # str의 첫번째 글자만 가져와서 3인지 6인지 9인지를 물으려고 했는데, 생각보다 str의 슬라이싱을 잡기가 어렵다.
    # 해당부분을 더 고안해야겠다.

