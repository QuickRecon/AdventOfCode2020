import re

inputFile = open("input", "r")

lines = inputFile.readlines()

validCount = 0
currentDict = {}
for line in lines:
    if line == '\n':
        currentDict = {}
        continue
    line = line.replace('\n', '')
    entries = line.split(' ')
    for entry in entries:
        (key, value) = entry.split(':')
        currentDict[key] = value
    if 'byr' in currentDict and 1920 <= int(currentDict['byr']) <= 2002\
            and 'iyr' in currentDict and 2010 <= int(currentDict['iyr']) <= 2020 \
            and 'eyr' in currentDict and 2020 <= int(currentDict['eyr']) <= 2030 \
            and 'hgt' in currentDict and (('cm' in currentDict['hgt'] and 150 <= int(re.match('[0-9]+',currentDict['hgt']).group()) <= 193) \
                                          or ('in' in currentDict['hgt'] and 59 <= int(re.match('[0-9]+',currentDict['hgt']).group()) <= 76))\
            and 'hcl' in currentDict and re.match('#[0-9a-f]{6}', currentDict['hcl']) and len(currentDict['hcl']) == 7\
            and 'ecl' in currentDict and currentDict['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']\
            and 'pid' in currentDict and re.match('[0-9]{9}', currentDict['pid']) and len(currentDict['pid']) == 9:
        validCount += 1
        print(currentDict)
        currentDict = {}

print(validCount)
