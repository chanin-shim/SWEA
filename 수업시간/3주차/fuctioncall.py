def func2():
    print("함수 2 시작")
    print("함수 2 끝")

def func1():
    print("함수 1 시작")
    func2()
    print("함수 1 시작")

print("메인시작")
func1()
print("메인끝")