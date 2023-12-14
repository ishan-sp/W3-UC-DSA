import math

def fibonacci(n):
    # Calculate nth Fibonacci number using the formula
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    fib_n = (phi**n - psi**n) / sqrt_5
    return int(fib_n)

def sum_of_squares_of_fibonacci(n):
    if n <= 0:
        return 0

    fib_n = fibonacci(n)
    fib_n_plus_1 = fibonacci(n + 1)

    # Sum of squares of Fibonacci numbers: Fib(n) * Fib(n+1)
    return fib_n * fib_n_plus_1

n = int(input())
print(sum_of_squares_of_fibonacci(n))
