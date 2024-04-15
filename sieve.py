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
    
    print(primes)

print("Enter a number to generate primes:")
n = int(input())

generatePrimes(n)