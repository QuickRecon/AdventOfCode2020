inputFile = open("input", "r")

lines = inputFile.readlines()

validCount = 0
for line in lines:
    # Break up each line into its constituent parts
    elements = line.split(':')
    password = elements[1].strip()
    rule = elements[0].split(' ')
    letter = rule[1]
    (lowerBound, upperBound) = rule[0].split('-')

    if int(lowerBound) <= password.count(letter) <= int(upperBound):
        validCount += 1

print(validCount)
