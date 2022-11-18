import math
import random

def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    else:
        return True

def get_prime(size, excluded = []):
    while True:
        p = random.randrange(size, 2*size)
        
        if (is_prime(p) and not p in excluded):
            return p

def lcm(a, b):
    return abs(a*b)//math.gcd(a, b)

def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e 
    else:
        return False

def get_d(e, lambda_n):
    for d in range(2, lambda_n):
        if (d*e) % lambda_n == 1:
            return d
    else:
        return False

# Key Generation by Alice
## Step 1: Generate two uniqe primes
size = 300
p = get_prime(size)
q = get_prime(size, [p])
print("p ", p, "and q ", q)
## Step 2: Compute n 
n = p * q
## Step 3: Compute lambda(n). Given n = pq, λ(n) = lcm(λ(p), λ(q)), and since p and q are prime, λ(p) = φ(p) = p − 1, and likewise λ(q) = q − 1. Hence λ(n) = lcm(p − 1, q − 1)
lambda_n = lcm(p-1, q-1)
## Step 4: Choose an integer e such that 1 < e < λ(n) and gcd(e, λ(n)) = 1; that is, e and λ(n) are coprime
e = get_e(lambda_n)
## Step 5: Determine d as d ≡ e−1 (mod λ(n)); that is, d is the modular multiplicative inverse of e modulo λ(n)
d = get_d(e, lambda_n)

# Done with Key Generation 
print("Public Key(e, n) = ", e, n)
print("Secret Key(d) = ", d)

# Bob sending a message to alice 
m = 117
print("message Bob = ", m)
c = m**e % n 
print("Public key encrypted message = ", c)
m = c**d % n
# Alice decrypting Bob's message
print("Decrypted by Alice = ", m)

# Eve sees the following
print("Eve sees (e ", e, ", n ", n, ", c ", c, " )")

def factor(n):
    for p in range(2, n):
        if n % p == 0:
            return p, n//p
    else:
        return None, None

p, q = factor(n)

print("Factors ", p, q)

if q == None or p == None:
    raise ValueError("q and p have to be Numbers") 

lambda_n = lcm(p-1, q-1)

e = get_e(lambda_n)
d = get_d(e, lambda_n)

print("Eve hacking it", c**d % n)
