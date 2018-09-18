import sys

high = 0

def sumOfProperDivs(num):
    i = 2
    maxVal = num
    total = 1

    while i <= maxVal / 2:
        if maxVal % i == 0:
            total += i
        i += 1

    return int(total)

def canBeSumOfTwoAbundants(num, abundants):
    global high
    while abundants[high] < num:
        high += 1

    searchArray = abundants[:high]

    for x in range(len(searchArray)):
        a = searchArray[x]
        for y in range(len(searchArray) - 1, x, -1):
            #print(y)
            b = searchArray[y]
            if a + b == num:
                print("%s + %s" % (a, b))
                return True
            elif a + b < num:
                break

    return False

def generateAllSums(abundants):
    sums = []

    for x in range(len(abundants)):
        print(abundants[x])
        for y in range(x, len(abundants)):
            sums.append(abundants[x] + abundants[y])

    return sums
        

if __name__ == "__main__":

    upperBound = 28170

    i = 12

    abundantNums = []

    print("Building all abundant nums under %s..." % upperBound)
    while i <= upperBound:
        if sumOfProperDivs(i) > i:
            abundantNums.append(i)
        i += 1

    total = 0

    print(abundantNums[:23])

    sums = generateAllSums(abundantNums)
    ints = [x for x in range(upperBound)]

    sumSet = set(sums)
    intSet = set(ints)

    answerSet = intSet.difference(sumSet)

    print(answerSet)
