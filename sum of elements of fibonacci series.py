def fibonacci_last_digit_sum_of_squares(n):
    if n <= 1:
        return n

    # Calculate the nth Fibonacci number modulo 60
    n_mod_60 = n % 60

    # Calculate the nth and (n+1)th Fibonacci numbers modulo 10
    fib_n_mod_10 = fib_n_plus_1_mod_10 = 1
    for i in range(2, n_mod_60 + 1):
        fib_n_mod_10, fib_n_plus_1_mod_10 = fib_n_plus_1_mod_10, (fib_n_mod_10 + fib_n_plus_1_mod_10) % 10

    # Calculate the last digit of the sum of squares of the first n Fibonacci numbers
    sum_of_squares_last_digit = (fib_n_mod_10 * fib_n_plus_1_mod_10) % 10

    return sum_of_squares_last_digit

# Example usage
n = int(input())  # Change this to the desired n
print(fibonacci_last_digit_sum_of_squares(n))
