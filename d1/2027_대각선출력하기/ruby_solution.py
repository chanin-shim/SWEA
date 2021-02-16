
ans = ['+'] * 5​
total = 0
​
while total <= 5:
    for j in range(5):
        ans[j] = '#'
        for k in ans:
            print("{}".format(k), end="")
            total += 1
            ans = ['+'] * 5
        print()


