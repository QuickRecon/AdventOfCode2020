def compare(index, password, letter):
    try:
        return password[int(index)-1] == letter
    except IndexError:
        return False


inputFile = open("input", "r")

lines = inputFile.readlines()

validCount = 0
for line in lines:
    # Break up each line into its constituent parts
    elements = line.split(':')
    password = elements[1].strip()
    rule = elements[0].split(' ')
    letter = rule[1]
    (lowerIndex, upperIndex) = rule[0].split('-')

    if compare(lowerIndex,password,letter) != compare(upperIndex,password,letter):
        validCount += 1

print(validCount)
