def push(item):
    s.append(item)
def pop():
    if len(s) == 0:
        print("비어있다")
        return
    else:
        return s.pop(-1)
s = []


push(1)
push(1)
push(2)
push(1)
push(4)
push(1)
push(1)
pop()
pop()
print(pop())
print(pop())
print(s)