from math import sqrt
import sys

def fibonacci(value):
    rho = (1 + sqrt(5)) / 2
    return int((rho**value - (-1/rho)**value) / sqrt(5))

if __name__ == "__main__":
    upperBound = int(sys.argv[1])

    i = 3

    fibValue = fibonacci(i)
    fibSum = 0
    while fibValue <= upperBound: 
        fibSum += fibValue
        i += 3
        fibValue = fibonacci(i)

    print(fibSum)
