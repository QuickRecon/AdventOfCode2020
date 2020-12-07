inputFile = open("input", "r")

lines = inputFile.readlines()

rightSkip = 3
downSkip = 1
trees = sum([element[1][int(element[0] * rightSkip / downSkip) % len(element[1])] == '#' for element in [(xindex, ylist) for xindex, ylist in enumerate([[i for i in j if not i == '\n'] for j in lines])] if element[0] % downSkip == 0])

print(trees)