'''
Created on Apr 28, 2009

@author: Brad
'''
import math

def triangleNum(n):
    return n * (n + 1) / 2

def isHexagonal(n):
    val = (math.sqrt(8*n + 1) + 1) % 4
    if val == 0:
        return True
    else:
        return False

def isPentagonal(n):
    val = (math.sqrt(24*n + 1) + 1) % 6
    if val == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    i = 286
    
    nextVal = 0
    while True:
        x = triangleNum(i)
        if isHexagonal(x) and isPentagonal(x):
            nextVal = x
            break
        i += 1
    
    print(nextVal)