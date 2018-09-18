import sys

def findPrimes(topPrime):
    primes = []
    primeArray = [True for x in range(0, topPrime/2 + 1)]

    primeArray[0] = False
    primeArray[1] = False

    thisFactor = 3
    lastSquare = 0
    thisSquare = 0

    count = 0

    while thisFactor * thisFactor <= topPrime:
        mark = thisFactor + thisFactor

        while mark <= topPrime / 2:
            primeArray[mark] = False
            mark += thisFactor

        thisSquare = thisFactor * thisFactor

        while lastSquare < thisSquare:
            if primeArray[lastSquare] == True:
                count += 1
                primes.append(lastSquare)
            lastSquare += 1

        thisFactor += 1

        while primeArray[thisFactor] == False:
            thisFactor += 1

    while lastSquare <= topPrime / 2:
        if primeArray[lastSquare] == True:
            count += 1
            primes.append(lastSquare)

        lastSquare += 1

    return primes

def sieve():
    current = 1
    primes = []
    yield 2
    while True:
        isPrime = True
        current += 2
        limit = current**.5
        for prime in primes:
            if (prime > limit):
                break
            if (current % prime == 0):
                isPrime = False
                break
        if isPrime:
            primes.append(current)
            yield current
    

if __name__ == "__main__":
    primeIndex = int(2000000)

    s = sieve()
    current = 0
    total = 0
    while current < primeIndex:
        current = s.next()
        total += current

    print(total)
