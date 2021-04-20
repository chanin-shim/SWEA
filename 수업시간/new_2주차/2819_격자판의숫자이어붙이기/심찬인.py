import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def make(x,y,c,num):
    global result
    if c == 6:
        if not num in result:
            result += [num]
        return

    if x+1 < 4:
        make(x+1,y,c+1,num+str(my_board[x+1][y]))
    if y+1 < 4:
        make(x,y+1,c+1,num+str(my_board[x][y+1]))
    if x - 1 >= 0:
        make(x-1,y,c+1,num+str(my_board[x-1][y]))
    if y - 1 >= 0:
        make(x,y-1,c+1,num+str(my_board[x][y-1]))

for tc in range(1, T+1):

    my_board = []
    for _ in range(4):
        my_board += [list(map(int,input().split()))]
    print(my_board)
    # [
    # [1, 1, 1, 1],
    # [1, 1, 1, 2],
    # [1, 1, 2, 1],
    # [1, 1, 1, 1]
    # ]

    result = []
    for x in range(4):
        for y in range(4):
            make(x,y,0,str(my_board[x][y]))

    print("#{} {}".format(tc,len(result)))