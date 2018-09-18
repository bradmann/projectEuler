import sys

def singleDigitToString(digit):
    if digit == "1":
        return "one"
    elif digit == "2":
        return "two"
    elif digit == "3":
        return "three"
    elif digit == "4":
        return "four"
    elif digit == "5":
        return "five"
    elif digit == "6":
        return "six"
    elif digit == "7":
        return "seven"
    elif digit == "8":
        return "eight"
    elif digit == "9":
        return "nine"

    return ""

def numberToString(num):
    numString = str(num)

    onesPlace = numString[len(numString) - 1]
    tensPlace = ""
    hundredsPlace = ""
    thousandsPlace = ""
    
    if len(numString) > 1:
        tensPlace = numString[len(numString) - 2]

    if len(numString) > 2:
        hundredsPlace = numString[len(numString) - 3]

    if len(numString) > 3:
        thousandsPlace = numString[len(numString) - 4]

    onesString = ""
    tensString = ""
    hundredsString = ""
    thousandsString = ""

    if onesPlace != "0":
        onesString = singleDigitToString(onesPlace)

    if tensPlace == "1":
        onesString = ""
        if onesPlace == "0":
            tensString = "ten"
        if onesPlace == "1":
            tensString = "eleven"
        if onesPlace == "2":
            tensString = "twelve"
        if onesPlace == "3":
            tensString = "thirteen"
        if onesPlace == "4":
            tensString = "fourteen"
        if onesPlace == "5":
            tensString = "fifteen"
        if onesPlace == "6":
            tensString = "sixteen"
        if onesPlace == "7":
            tensString = "seventeen"
        if onesPlace == "8":
            tensString = "eighteen"
        if onesPlace == "9":
            tensString = "nineteen"
    if tensPlace == "2":
        tensString = "twenty"
    if tensPlace == "3":
        tensString = "thirty"
    if tensPlace == "4":
        tensString = "forty"
    if tensPlace == "5":
        tensString = "fifty"
    if tensPlace == "6":
        tensString = "sixty"
    if tensPlace == "7":
        tensString = "seventy"
    if tensPlace == "8":
        tensString = "eighty"
    if tensPlace == "9":
        tensString = "ninety"

    if hundredsPlace != "":
        hundredsString = singleDigitToString(hundredsPlace)
        if hundredsString != "":
            hundredsString += "hundred"

        if tensPlace != "0" or onesPlace != "0":
            hundredsString += "and"

    if thousandsPlace != "":
        thousandsString = singleDigitToString(thousandsPlace)
        thousandsString += "thousand"

    return thousandsString + hundredsString + tensString + onesString
    

if __name__ == "__main__":
    value = int(sys.argv[1])

    total = 0

    for x in range(1, value + 1):
        val = numberToString(x)
        print(val)
        total += len(val)

    print(total)
