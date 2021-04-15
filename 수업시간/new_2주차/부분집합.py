A = [-1, 3, -9, 6, 7, -6, 7, -6, 1, 5, 4, -2]

for i in range(1<<10):
    s = 0
    for j in range(10):
        if i&(1<<j):
            s += A[j]
    if s==0:
        for j in range(10):
            if i & (1 << j):
                print(A[j], end=' ')
        print()