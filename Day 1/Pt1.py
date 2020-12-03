inputFile = open("input", "r")

numberList = inputFile.readlines()

for str1 in numberList:
    for str2 in numberList:
        num1 = int(str1)
        num2 = int(str2)
        if num1 + num2 == 2020:
            print("Num1 :" + str(num1))
            print("Num2 :" + str(num2))
            print("Num1 * Num2: " + str(num1 * num2))
