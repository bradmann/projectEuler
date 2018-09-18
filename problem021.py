import sys

def sumOfProperDivs(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i

    return total

if __name__ == "__main__":
    num = int(sys.argv[1])

    total = 0

    for i in range(num):
        value = sumOfProperDivs(i)

        if sumOfProperDivs(value) == i and value != i:
            print(str(value) + ", " + str(i))
            total += value + i

    print(total / 2)
