def fibonacci(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        t1 = 1
        t2 = 1
        for j in range(0,n-2):
            t3 = t1 + t2
            t1 = t2
            t2 = t3
        return t3
num = int(input())
print(fibonacci(num))

