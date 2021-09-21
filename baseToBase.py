import other.functions as functions # functions.py

while True :
    num = int(input("Enter number to convert:\n"))
    startingBase = int(input("What base is this number in?:\n"))
    endingBase = int(input("What base would you like to convert it to?:\n"))

    if startingBase < 2 or startingBase > 10 :
        print("ERROR: this program cannot handle base", str(startingBase), "as the starting base")
        continue
    if endingBase < 2 or endingBase > functions.bigNumLen() + 10 :
        print("ERROR: this program cannot handle base", str(endingBase))
        continue

    fbreak = False
    for number in str(num) :
        if int(number) >= startingBase :
            print("ERROR: given number is in a higher base than specified")
            fbreak = True
            break

    if fbreak == True :
        continue

    if endingBase >= 10 :
        newNum = functions.upFromTen(int(functions.toBaseTen(str(num), startingBase)), endingBase)
    else :
        newNum = functions.fromBaseTen(int(functions.toBaseTen(str(num), startingBase)), endingBase)
    print("the base", startingBase, "number", num, "in base", endingBase, "is", newNum)
