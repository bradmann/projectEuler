'''
Created on Apr 16, 2009

@author: mannb
'''

import math

def isPrime(num):
    max = math.ceil(math.sqrt(num))  
    if num == 2:
        return True
    if num % 2 == 0 or num == 1:
        return False
    for i in range(3, max + 1, 2):
        if num % i == 0:
            return False 
    return True

def isLTRPrime(num):
    numString = str(num)
    if len(numString) == 1:
        if isPrime(num):
            return True
        else:
            return False
    else:
        if isPrime(num):
            newNum = int(numString[1:])
            return isLTRPrime(newNum)
        else:
            return False
        
def isRTLPrime(num):
    numString = str(num)
    if len(numString) == 1:
        if isPrime(num):
            return True
        else:
            return False
    else:
        if isPrime(num):
            newNum = int(numString[:-1])
            return isRTLPrime(newNum)
        else:
            return False
        
def isTruncatablePrime(num):
    if isPrime(num) and isLTRPrime(num) and isRTLPrime(num):
        return True
    else:
        return False

if __name__ == '__main__':
    count = 0
    i = 8
    truncatablePrimes = []
    while count < 11:
        if isTruncatablePrime(i):
            print(i)
            count += 1
            truncatablePrimes.append(i)
        i += 1
        
    total = sum(truncatablePrimes)
    
    print("Sum of truncatable primes: %s" % total)