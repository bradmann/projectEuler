from math import sqrt
import sys

if __name__ == "__main__":
    numDigits = int(sys.argv[1])

    first = 0
    nxt = 1

    fib = str(first + nxt)

    counter = 1

    while len(fib) != numDigits:
        counter += 1
        print(fib)
        tmp = nxt
        nxt = first + nxt
        first = tmp
        fib = str(nxt)

    print(counter)
    
