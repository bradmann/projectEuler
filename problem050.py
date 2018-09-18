'''
Created on Apr 29, 2009

@author: Brad
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
        
def nextPrime(n):
    i = n + 1
    while True:
        if isPrime(i):
            return i
        i += 1

if __name__ == '__main__':
    longest = 0
    prime = 0
    startPrime = 2
    
    while startPrime < math.ceil(1000000 / 2):
        np = startPrime
        seq = [startPrime]
        while sum(seq) < 1000000:
            np = nextPrime(np)
            seq.append(np)
            if isPrime(sum(seq)):
                if len(seq) > longest:
                    longest = len(seq)
                    prime = sum(seq)
                    print(longest)
                    print(prime)
        startPrime = nextPrime(startPrime)
        
    print(longest)
    print(prime)