import math
def compute_gcd(a, b):
    return math.gcd(a, b)
a, b = map(int, input().split())


gcd_result = compute_gcd(a, b)
print(gcd_result)
