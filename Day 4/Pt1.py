inputFile = open("input", "r")

lines = inputFile.readlines()

validCount = 0
currentDict = {}
for line in lines:
    if line == '\n':
        currentDict = {}
        continue
    line.replace('\n', '')
    entries = line.split(' ')
    for entry in entries:
        (key, value) = entry.split(':')
        currentDict[key] = value
    if 'byr' in currentDict and 'iyr' in currentDict and 'eyr' in currentDict and 'hgt' in currentDict \
            and 'hcl' in currentDict and 'ecl' in currentDict and 'pid' in currentDict:
        validCount += 1
        currentDict = {}

print(validCount)
