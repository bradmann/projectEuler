'''
Created on Apr 28, 2009

@author: Brad
'''

if __name__ == '__main__':
    hugeNumber = 0
    for i in range(1, 1001):
        hugeNumber += i**i
    
    hugeNumberString = str(hugeNumber)
    print(hugeNumberString[-10:])