import sys
sys.stdin = open("input.txt")

T = int(input())

def battle(arr):
    global stack
    for i in arr:
        if not len(stack):
            stack.append(i)
        else:
            v = stack.pop
            if v == i: #무승부라면, 뒤에 들어온게 이김
                stack.append(i)
            if v ==1 and i == 2:
                stack.append(2)
            if v ==2 and i == 1:
                stack.append(2)
            if v ==2 and i == 3:
                stack.append(3)
            if v ==3 and i == 2:
                stack.append(3)
            if v ==3 and i == 1:
                stack.append(1)
            if v ==1 and i == 3:
                stack.append(1)

    # print(stack)




for tc in range(1, T+1):
    N = int(input())
    students = list(map(int,input().split()))

    # print(students)
    # [1, 3, 2, 1]

    a_group = []
    b_group = []

    for i in range(len(students)):
        if len(students) % 2 == 0: # 전체 학생수가 짝수이고
            if i < len(students)//2: # 학생수//2 보다 i가 작다면
                a_group += [students[i]]
            if i >= len(students)//2:
                b_group += [students[i]]

        else: #홀수일때
            if i <= len(students)//2: # 학생수//2 보다 i가 작다면
                a_group += [students[i]]
            if i > len(students)//2:
                b_group += [students[i]]

    stack = []
    # print(a_group)
    # print(b_group)
    # [1, 3]
    # [2, 1]
    battle(a_group)
    final_grup = []
    final_grup += stack
    stack = []
    battle(b_group)
    final_grup += stack

    print(final_grup)

    # tc2일 때, b그룹 2,3,3이 잘못나오지?
    # 3나와야하는데 2로 나옴.