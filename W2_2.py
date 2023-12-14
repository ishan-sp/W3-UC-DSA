def multiply(A, B):
    """Helper function to multiply two matrices."""
    return [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
    ]

def power(matrix, n):
    """Helper function to calculate matrix power."""
    if n == 1:
        return matrix
    elif n % 2 == 0:
        half_power = power(matrix, n // 2)
        return multiply(half_power, half_power)
    else:
        return multiply(matrix, power(matrix, n - 1))

def fibonacci_last_digit(n):
    if n <= 1:
        return n

    base_matrix = [[1, 1], [1, 0]]
    result_matrix = power(base_matrix, n - 1)
    return result_matrix[0][0] % 10

num = int(input())
print(fibonacci_last_digit(num))
