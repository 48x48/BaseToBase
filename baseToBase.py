import math

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

while True :
    num = int(input("Enter number to convert:\n"))
    startingBase = int(input("What base is this number in?:\n"))
    endingBase = int(input("What base would you like to convert it to?:\n"))

    if startingBase < 2 or startingBase > 10 :
        print("ERROR: there is no such thing as base", str(startingBase) + ", or if there is, this program can't handle it")
        continue
    if endingBase < 2 or endingBase > 10 :
        print("ERROR: there is no such thing as base", str(endingBase) + ", or if there is, this program can't handle it")
        continue

    fbreak = False
    for number in str(num) :
        if int(number) >= startingBase :
            print("ERROR: given number is in a higher base than specified")
            fbreak = True
            break

    if fbreak == True :
        continue

    newNum = fromBaseTen(int(toBaseTen(str(num), startingBase)), endingBase)
    print("the base", startingBase, "number", num, "in base", endingBase, "is", newNum)
