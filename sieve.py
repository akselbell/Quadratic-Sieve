from functions import checkSmooth, gcd, generatePrimes, mod2
from matrix_functions import null_space_mod2, transpose
from datetime import datetime
import math

def calcXY():
    squares = []
    for i in range(len(linearCombination)):
        if linearCombination[i] == 1:
            squares.append(keys[i])

    totalExponents = []
    for i in range(len(primes)):
        entry = 0
        for j in squares:
            entry = entry + factorizations[j][i]
        totalExponents.append(entry)

    #print(totalExponents)
        
    squaresProduct = 1
    primesProduct = 1

    for i in range(len(squares)):
        squaresProduct = squaresProduct * squares[i]

    for i in range(len(totalExponents)):
        if totalExponents[i] != 0:
            power = totalExponents[i] // 2  # Calculate the exponent
            result = primes[i] ** power % n  # Compute the result modulo n
            primesProduct = primesProduct * result
    
    return [squaresProduct, primesProduct]


#use 268905821 as an example input, it factors to 14347 * 18743
#or 4994399 or 1491858941, or 315162571127
print("Enter a number to factor:")
n = int(input())

timeLastChecked = datetime.now()

#B = int(math.sqrt(n))
B = math.ceil(math.exp(0.5 * math.sqrt(math.log(n) * math.log(math.log(n)))))
primes = generatePrimes(B, n)

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
        print(len(keys))
    
    i = i + 1

# print(datetime.now() - timeLastChecked)
# timeLastChecked = datetime.now()

transposedMatrix = transpose(matrix)
nullSpace = null_space_mod2(transposedMatrix)

# print(datetime.now() - timeLastChecked)
# timeLastChecked = datetime.now()

xySquaresDif = 0
xyDif = 0
xySum = 0
i = 0
factor1 = 1
while factor1 == 1:
    linearCombination = nullSpace[i] # the linear combination of exponent vectors that sum to zero vector

    squaresProduct, primesProduct = calcXY()  # call the function and unpack the return values
    xySquaresDif = (squaresProduct * squaresProduct - primesProduct * primesProduct) % n
    xyDif = abs(squaresProduct - primesProduct) % n
    xySum = (squaresProduct + primesProduct) % n
    #print("xySquaresDif " + str(xySquaresDif)) # should ALWAYS be equal to zero
    print("xyDif " + str(xyDif))
    print("xySum " + str(xySum))

    if xyDif != 0 and xySum != 0:
        factor1 = gcd(xyDif, n)

    #print(str(xySquaresDif) + " " + str(xyDif) + " " + str(xySum) + " " + str(factor1))
    i += 1

print(datetime.now() - timeLastChecked)
factor2 = n // factor1
print("Factor 1: " + str(factor1))
print("Factor 2: " + str(factor2))