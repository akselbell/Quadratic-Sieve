def checkSmooth(n, primes_set):
    exponents = [0] * len(primes_set)
    for i, prime in enumerate(primes_set):
        while n % prime == 0:
            exponents[i] += 1
            n //= prime
            if n == 1:
                return exponents
    return []

## below is skeleton of code that could use paralell processing to check if b smooth, going to edit to have it
##fit our algorithm in the morning
##def worker(n, primes):
    original_n = n
    for prime in primes:
        while n % prime == 0:
            n //= prime
            if n == 1:
                return True, original_n  # Successfully divided completely
    return False, n  # Not completely divisible, return remaining n

##def is_b_smooth_parallel(n, B):
    primes = sieve_of_eratosthenes(B)
    chunks = [primes[i::4] for i in range(4)]  # Assuming 4 workers, adjust based on your CPU

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(worker, [n] * len(chunks), chunks)
        
        for is_divisible, remaining_n in results:
            if is_divisible:
                return True  # n is B-smooth
            n = remaining_n  # Update n based on the last non-divisible result
        
    return n == 1  

def gcd(x,y): # Euclid's algorithm
     if y == 0:
         return x
     elif x >= y:
         return gcd(y,x % y)
     else:
         return gcd(y,x) 


def mod2(exponentVector):
    return [i % 2 for i in exponentVector]


def generatePrimes(B, n):
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
            #if legendre_symbol(n, i) == 1:
            ret.append(i)

    return ret

def legendre_symbol(n, p):
    ls = pow(n, (p - 1) // 2, p)
    return ls