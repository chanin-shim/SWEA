# 클래스로 스택 만들기

aa = '()()((())))'

class Stack():
    stack = []

    def push(self, data):  # ~를 넣어줘. 즉 ~라는 인자를 넣어야함 (그것이 바로 data)
        self.stack.append(data)
        return self.stack

    def pop(self):  # 마지막걸 빼줘. 즉 인자가 필요없음.
        data = self.stack.pop()
        return data

real_list = list(map(str,aa))
s = Stack()

for i in real_list:
    print(s.push('{}'.format(i)))
print(s.stack)
print(s.pop())
print(s.stack)
print(s.pop())
print(s.stack)
print(s.pop())
print(s.stack)
print(s.pop())
print(s.stack)
print(s.pop())