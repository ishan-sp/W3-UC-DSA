def fibonacci(n,m):
    l1 = [1,1]+([0]*(m-2))
    for i in range(2, m):
        l1[i] = l1[i-1] + l1[i-2]
    l2 = l1[n-1:m]
    return str(sum(l2))[-1]
num1, num2 = map(int, input().split())
print(fibonacci(num1,num2))





