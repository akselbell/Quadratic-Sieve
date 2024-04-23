def checkSmooth(n, primes_set):
    exponents = [0] * len(primes_set)
    for i, prime in enumerate(primes_set):
        while n % prime == 0:
            exponents[i] += 1
            n //= prime
            if n == 1:
                return exponents
    return []

def gcd(x,y): # Euclid's algorithm
     if y == 0:
         return x
     elif x >= y:
         return gcd(y,x % y)
     else:
         return gcd(y,x) 


def mod2(exponentVector):
    return [i % 2 for i in exponentVector]


def generatePrimes(B):
    if B < 2:
        return []

    primes = [True] * (B + 1)
    primes[0] = primes[1] = False
    
    # Start with 3 and iterate through odd numbers
    p = 3
    while p * p <= B:
        if primes[p]:
            # Mark multiples of p starting from p*p
            for i in range(p * p, B + 1, 2 * p):
                primes[i] = False
        p += 2
    
    ret = [2]  # 2 is prime, but not included in the sieve
    for i in range(3, B + 1, 2):
        if primes[i]:
            ret.append(i)

    return ret

# if primes[i] and legendre_symbol(n, i) == 1:
#             ret.append(i)

#     return ret

# def legendre_symbol(n, p):

#     ls = pow(n, (p - 1) // 2, p)
#     if ls == p - 1:
#         return -1
#     return ls