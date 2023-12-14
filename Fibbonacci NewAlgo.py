import time
def fibonacci(n):
    l1 = [1,1]+([0]*(n-2))
    # [0,1,0,0,0,0,0,0,0,0,0,0...]
    for i in range(2, n):
        l1[i] = l1[i-1] + l1[i-2]
    return l1[-1]
start_time = time.time()
print(fibonacci(1000))
end_time = time.time()
print(end_time - start_time)

#1,1,2,3,5
#0,1,1,2,3,5
