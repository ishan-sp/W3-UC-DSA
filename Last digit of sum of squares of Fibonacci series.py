import math

def fibonacci(n):
    l1 = [1,1]+([0]*(n-2))
    for i in range(2, n):
        l1[i] = l1[i-1] + l1[i-2]
    return l1[-1]


def sum_of_squares_of_fibonacci(n):
    if n <= 0:
        return 0

    fib_n = fibonacci(n)
    fib_n_plus_1 = fibonacci(n + 1)

    # Sum of squares of Fibonacci numbers: Fib(n) * Fib(n+1)
    return fib_n * fib_n_plus_1

n = int(input())
print(str(sum_of_squares_of_fibonacci(n))[-1])
