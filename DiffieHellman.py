import math

def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    else:
        return True

print(is_prime(22))

