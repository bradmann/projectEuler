'''
Created on Apr 28, 2009

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

def arePermutations(numbers):
    numString1 = str(numbers[0])
    numString2 = str(numbers[1])
    numString3 = str(numbers[2])
    
    if len(numString1) != len(numString2) or len(numString1) != len(numString3) or len(numString2) != len(numString3):
        return False
    
    numString = str(numbers[0])
    
    for n in numbers[1:]:
        num = str(n)
        for c in num:
            if c not in numString:
                return False
            
    numString = str(numbers[1])
    
    for n in [numbers[0], numbers[2]]:
        num = str(n)
        for c in num:
            if c not in numString:
                return False
            
    numString = str(numbers[2])
    
    for n in [numbers[0], numbers[1]]:
        num = str(n)
        for c in num:
            if c not in numString:
                return False
    return True

if __name__ == '__main__':
    start = 1488
    sequence = []
    found = False
    while not found:
        maxIncrease = int((10000 - start)/2)
        for i in range(start, maxIncrease):
            x = start
            y = start + i
            z = start + i + i
            sequence = [x, y, z]
            if isPrime(x) and isPrime(y) and isPrime(z) and arePermutations(sequence):
                found = True
                break
        start += 1
        
    print(sequence)