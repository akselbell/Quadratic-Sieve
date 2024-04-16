from functions import checkSmooth, gcd, generatePrimes
import math

print("Enter a number to generate primes:")
n = int(input())

B = 100
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
factorizations = dict() # map of each x^2 term that is B smooth
sievingInterval = [math.floor(math.sqrt(n)) - B, math.floor(math.sqrt(n)) + B]

for i in range(sievingInterval[0], sievingInterval[1]):
    if len(factorizations) > len(primes):
        break
    
    x = (i * i) % n
    exponentsVector = checkSmooth(x, primes)

    if(len(exponentsVector) != 0):
        factorizations[i] = exponentsVector
    




print(checkSmooth(n, primes))
