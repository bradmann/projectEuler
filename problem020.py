import sys

def factorial(num):
    if (num == 1):
        return 1
    else:
        return num * factorial(num - 1)

if __name__ == "__main__":

    num = int(sys.argv[1])

    value = str(factorial(num))

    total = 0

    for x in value:
        total += int(x)

    print(total)

    
