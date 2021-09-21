import math, json

bigNumbers = json.loads(open("other/bigNumbers.json").read())
keys = list(bigNumbers.keys())
values = list(bigNumbers.values())

def bigNumLen() :
    return len(bigNumbers)

def toBaseTen(n, startBase) :    # n must be a string
    numOn = len(n) - 1
    count = 0
    total = 0.0
    while numOn >= 0 :
        total += float(n[numOn]) * math.pow(float(startBase), count)
        numOn -= 1
        count += 1
    return total

def fromBaseTen(n, targetBase) :
    final = ""

    powerNum = 0
    baseRaised = 0
    while baseRaised <= n :
        powerNum += 1
        baseRaised = math.pow(float(targetBase), powerNum)
    powerNum -= 1
    baseRaised = math.pow(float(targetBase), powerNum)

    multiplier = 1
    while baseRaised * multiplier <= n :
        multiplier += 1
    baseRaised *= multiplier - 1
    final += str(multiplier - 1)
    n -= baseRaised

    while powerNum > 0 :
        powerNum -= 1
        baseRaised = math.pow(float(targetBase), powerNum)

        multiplier = 0
        while baseRaised * multiplier <= n :
            multiplier += 1
        multiplier -= 1
        final += str(multiplier)
        n -= baseRaised * multiplier

    return final

def upFromTen(n, targetBase) :
    quotient = n // targetBase
    remainder = []
    if n % targetBase < 10 :
        remainder.append(n % targetBase)
    else :
        remainder.append(values.index(n % targetBase))

    part = 0
    while quotient != 0 :
        part += 1
        if quotient % targetBase < 10 :
            remainder.append(quotient % targetBase)
        else :
            remainder.append(keys[values.index(quotient % targetBase)])
        quotient = quotient // targetBase

    result = ""
    i = len(remainder) - 1
    while i >= 0 :
        result += str(remainder[i])
        i -= 1
    return result
