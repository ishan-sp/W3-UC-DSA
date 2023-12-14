def fibonacci(n):
    init = 0
    l1 = [1, 1]+([0]*(n-2))
    for i in range(2, n):
        l1[i] = l1[i-1] + l1[i-2]
    last_num = l1[-1]
    return str(last_num)[-1]
n = int(input("Enter a number : "))
print(fibonacci(n))



