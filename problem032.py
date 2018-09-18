import sys

def identityIsPandigital(x, y):
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    z = x * y

    m1 = str(x)
    m2 = str(y)
    p = str(z)

    if len(m1) + len(m2) + len(p) != 9:
        return False

    for a in m1:
        if a in digits:
            digits.remove(a)
        else:
            return False

    for b in m2:
        if b in digits:
            digits.remove(b)
        else:
            return False

    for c in p:
        if c in digits:
            digits.remove(c)
        else:
            return False

    if len(digits) > 0:
        return False
    else:
        return True

if __name__ == "__main__":

    pandigitals = []
    total = 0
    
    for i in range(2000):
        for j in range(2000):
            if identityIsPandigital(i, j):
                product = i*j
                if product not in pandigitals:
                    pandigitals.append(product)

    for x in pandigitals:
        total += x

    print(total)
