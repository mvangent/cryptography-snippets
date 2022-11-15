import math
import random

def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    else:
        return True

def get_prime(size):
    while True:
        p = random.randrange(size, 2*size)
        
        if (is_prime(p)):
            return p

def is_generator(g, p):
    for i in range (1, p - 1):
        if (g**i) % p == 1:
            return False
    else:
        return True 

def get_generator(p):
    for g in range(2, p):
        if is_generator(g, p):
            return g
    else:
        raise ValueError("No generator found for", p)

# Public
prime = get_prime(11000)
generator = get_generator(prime)

print(prime, generator)

# Alice
a = random.randint(1, prime)
a_g = (generator**a) % prime

print("Alice", " a:", a, "generated with a ", a_g)

# Bob
b = random.randint(1, prime)
b_g = (generator**b) % prime
print("Bob", " b:", b, "generated with b ", b_g)

# Alice 
print((b_g**a) % prime)

# Bob
print((a_g**b) % prime)

