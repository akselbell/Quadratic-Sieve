from functions import checkSmooth, gcd, generatePrimes, mod2
from matrix_functions import null_space_mod2, transpose
from datetime import datetime
import math

def quadratic_sieve(n):
    start_time = datetime.now()

    B = int(math.sqrt(n)) + 100000  # Adjust B based on the input size
    primes = generatePrimes(B)
    primes_set = set(primes)

    print("Prime generation time:", datetime.now() - start_time)
    start_time = datetime.now()

    factorizations = {}  # Map of each x^2 term that is B-smooth
    sieving_interval = [int(math.sqrt(n)), int(math.sqrt(n)) + B]
    keys = []
    matrix = []

    for i in range(sieving_interval[0], sieving_interval[1]):
        if len(factorizations) > len(primes):
            break
        
        x = (i * i) % n
        exponents_vector = checkSmooth(x, primes_set)

        if exponents_vector:
            keys.append(i)
            factorizations[i] = exponents_vector
            matrix.append(mod2(exponents_vector))

    print("Sieving time:", datetime.now() - start_time)
    start_time = datetime.now()

    transposed_matrix = transpose(matrix)
    null_space = null_space_mod2(transposed_matrix)

    print("Null space computation time:", datetime.now() - start_time)
    start_time = datetime.now()

    linear_combination = null_space[0]
    squares = [keys[i] for i in range(len(linear_combination)) if linear_combination[i] == 1]

    squares_product = 1
    primes_product = 1

    for square in squares:
        squares_product *= square
        exponents = factorizations[square]
        for j in range(len(exponents)):
            if exponents[j] != 0:
                primes_product *= primes[j] ** (exponents[j] // 2)

    dif = abs(squares_product - primes_product) % n
    factor1 = gcd(dif, n)
    factor2 = n // factor1

    print("Factorization time:", datetime.now() - start_time)
    print("Factor 1:", factor1)
    print("Factor 2:", factor2)

# Example usage:
print("Enter a number to factor:")
n = int(input())
quadratic_sieve(n)
