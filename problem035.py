import math

def rotateNum(numString):
    tmp = numString[0]
    numString = numString[1:]
    numString += tmp
    return numString

def isPrime(num):
    upper = int(math.sqrt(abs(num)))

    if num < 0:
        for i in range(2, -upper - 1, -1):
            if num % i == 0:
                return False
    else:
        for i in range(2, upper + 1):
            if num % i == 0:
                return False

    return True

if __name__ == "__main__":
    circPrimes = []
    
    for i in range(2, 1000000):
        if isPrime(i):
            rotationsAreAllPrime = True

            numString = str(i)
            if len(numString) > 1:
                newNum = str(i)
                for x in range(len(numString)):
                    newNum = rotateNum(newNum)
                    if not isPrime(int(newNum)):
                        rotationsAreAllPrime = False
                        break
            if rotationsAreAllPrime:
                circPrimes.append(i)

    print(circPrimes)
    print(len(circPrimes))
