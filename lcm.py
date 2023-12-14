import math

def compute_lcm(a, b):
    # LCM(a, b) = (a * b) / GCD(a, b)
    return (a * b) // math.gcd(a, b)

a, b = map(int, input().split())


lcm_result = compute_lcm(a, b)
print(lcm_result)
