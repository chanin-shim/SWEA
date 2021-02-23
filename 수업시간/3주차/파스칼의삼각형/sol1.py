import sys
sys.stdin = open("input.txt")

T = int(input())

class stack():
    stack = []

    def push(self,data):
        self.stack.append(data)
        return self.stack

    def pop(self):
        data = self.stack.pop()
        return data

s = stack()
for tc in range(1, T+1):

    N = int(input())

    s.push(1)
    print(s.stack)

    # stack이 2개 쌓여있으면 더해라, 아니라면 1만 나와




    print("#{} ".format(tc, ))