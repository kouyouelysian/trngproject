'''
    TRNG PROJECT - DEMO PROGRAM: RANDOM PRIME NUMBER GENERATOR
'''

import random
import math
from trnglib import trng

# checks if a number is prime
def checkPrime(n, trng, length_bytes=16, k=128):
    # detect obvious cases
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        # a = randrange(2, n - 1)
        a = int.from_bytes((trng.getRandomBytesArray(length_bytes)), 'big')
        if (a > n):
            a -= n
        if (a < 2):
            a = 2
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while ((j < s) and (x != n - 1)):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True



# returns a prime number
def generatePrime(trng, length=128):
    if not (length % 8 == 0):
        raise ValueError("bad key length!")
    length_bytes = int(length/8)
    p = 4
    while not checkPrime(p, trng, length_bytes, 128):
        p = int.from_bytes((trng.getRandomBytesArray(length_bytes)), 'big')
        p |= (1 << length - 1)
        p |= 1
        print("tried for prime", p)
    print("\nfound prime:", p, "\n\n")
    return p


# main run
if (__name__ == "__main__"):

    device = trng(portname="/dev/cu.wchusbserialfd120")
    device.connect()

    primes = []
    for x in range(4):
        primes.append(generatePrime(device))

    device.disconnect()

    print("final list of primes is:\n")
    for p in primes:
        print(p)
    