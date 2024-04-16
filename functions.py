def checkSmooth(n, primes):
    # trial division pretty much, might be useful to add check at top if the number is B smooth using the stack forum
    i = 0
    exponents = [0] * len(primes)
    while n != 1:
        if i > len(primes)-1:
            return []
        while n % primes[i] == 0:
            exponents[i] += 1
            n = n / primes[i]
        i += 1
    return exponents


def gcd(x,y): # Euclid's algorithm
     if y == 0:
         return x
     elif x >= y:
         return gcd(y,x % y)
     else:
         return gcd(y,x) 

def generatePrimes(B):
    #sieve of Eratosthenes
    if(B < 2):
        return []

    primes = [True] * (B + 1)
    primes[0] = primes[1] = False
    p = 2
    
    while(p*p <= B):
        i = p*p
        while(i <= B):
            primes[i] = False
            i = i + p
        
        p = p + 1
        while not primes[p]:
            p = p + 1
    
    ret = []
    for i in range(len(primes)):
        if(primes[i]):
            ret.append(i)

    return ret

def mod2(exponentVector):
    return [i % 2 for i in exponentVector]