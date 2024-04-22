from functions import checkSmooth, gcd, generatePrimes, mod2
from matrix_functions import null_space_mod2, transpose
from datetime import datetime
import math
#import sympy

#use 268905821 as an example input, it factors to 14347 * 18743
#or 4994399
print("Enter a number to factor:")
n = int(input())

timeLastChecked = datetime.now()

B = int(math.sqrt(n))
#B = math.ceil(math.exp(0.5 * math.sqrt(math.log(n) * math.log(math.log(n)))))
primes = generatePrimes(B)

print(datetime.now() - timeLastChecked)
timeLastChecked = datetime.now()

factorizations = dict() # map of each x term who's x^2 term is B smooth
i = math.ceil(math.sqrt(n))
keys = []
matrix = []

while len(factorizations) <= len(primes):
    x = (i * i) % n
    exponentsVector = checkSmooth(x, primes)

    if(len(exponentsVector) != 0):
        keys.append(i)
        factorizations[i] = exponentsVector
        matrix.append(mod2(exponentsVector))
    
    i = i + 1

print(datetime.now() - timeLastChecked)
timeLastChecked = datetime.now()

transposedMatrix = transpose(matrix)
nullSpace = null_space_mod2(transposedMatrix)

print(datetime.now() - timeLastChecked)
timeLastChecked = datetime.now()

linearCombination = nullSpace[0] # the linear combination of exponent vectors that sum to zero vector
squares = []

for i in range(len(linearCombination)):
    if linearCombination[i] == 1:
        squares.append(keys[i])

#print(squares)

squaresProduct = 1
primesProduct = 1

for i in range(len(squares)):
    squaresProduct = squaresProduct * squares[i]
    
    exponents = factorizations[squares[i]]
    print(str(squares[i]) + "    " + str(exponents))
    for j in range(len(exponents)):
        if exponents[j] != 0:
            primesProduct = primesProduct * (primes[j] ** exponents[j])    

print((primesProduct - squaresProduct*squaresProduct)%n) # should ALWAYS be equal to zero

primesProduct = math.sqrt(primesProduct)
dif = abs(squaresProduct - primesProduct) % n

print(dif)
factor1 = gcd(dif, n)
print(factor1)
factor2 = n / factor1
print(factor2)