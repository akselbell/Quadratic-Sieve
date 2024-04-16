from functions import checkSmooth, gcd, generatePrimes, mod2
import math
#import sympy

#use 3431 as an example input, it factors to 47 * 73
print("Enter a number to factor:")
n = int(input())

B = 100
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
factorizations = dict() # map of each x^2 term that is B smooth
sievingInterval = [math.ceil(math.sqrt(n)), math.floor(math.sqrt(n)) + B]
matrix = []

for i in range(sievingInterval[0], sievingInterval[1]):
    if len(factorizations) > len(primes):
        break
    
    x = (i * i) % n
    exponentsVector = checkSmooth(x, primes)

    if(len(exponentsVector) != 0):
        factorizations[i] = exponentsVector
        matrix.append(mod2(exponentsVector))
        #they are currently added row vectors i think?

print(matrix)