import math

def fibonacci(n):
    if n <= 1:
        return n

    # Initialize variables to store the previous two Fibonacci numbers
    fib_prev = 0
    fib_current = 1

    # Iterate to calculate the nth Fibonacci number
    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_current
        fib_prev, fib_current = fib_current, fib_next

    return fib_current
def sum_of_squares_of_fibonacci(n):
    if n <= 0:
        return 0

    fib_n = fibonacci(n)
    fib_n_plus_1 = fibonacci(n + 1)

    # Sum of squares of Fibonacci numbers: Fib(n) * Fib(n+1)
    return fib_n * fib_n_plus_1

n = int(input())
print(str(sum_of_squares_of_fibonacci(n))[-1])
