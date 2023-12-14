import time
def fibonacci(n):
    l1 = [1,1]+([0]*(n-2))
    for i in range(2, n):
        l1[i] = l1[i-1] + l1[i-2]
    y = str(sum(l1))
    return str(sum(l1))[-1]
start_time = time.time()
print(fibonacci(100))
end_time = time.time()
print(end_time - start_time)


