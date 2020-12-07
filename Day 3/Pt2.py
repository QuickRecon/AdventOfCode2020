inputFile = open("input", "r")

lines = inputFile.readlines()

rightSkip = 1
downSkip = 1
trees1 = sum([element[1][int(element[0] * rightSkip / downSkip) % len(element[1])] == '#' for element in [(xindex, ylist) for xindex, ylist in enumerate([[i for i in j if not i == '\n'] for j in lines])] if element[0] % downSkip == 0])

rightSkip = 3
downSkip = 1
trees2 = sum([element[1][int(element[0] * rightSkip / downSkip) % len(element[1])] == '#' for element in [(xindex, ylist) for xindex, ylist in enumerate([[i for i in j if not i == '\n'] for j in lines])] if element[0] % downSkip == 0])

rightSkip = 5
downSkip = 1
trees3 = sum([element[1][int(element[0] * rightSkip / downSkip) % len(element[1])] == '#' for element in [(xindex, ylist) for xindex, ylist in enumerate([[i for i in j if not i == '\n'] for j in lines])] if element[0] % downSkip == 0])

rightSkip = 7
downSkip = 1
trees4 = sum([element[1][int(element[0] * rightSkip / downSkip) % len(element[1])] == '#' for element in [(xindex, ylist) for xindex, ylist in enumerate([[i for i in j if not i == '\n'] for j in lines])] if element[0] % downSkip == 0])

rightSkip = 1
downSkip = 2
trees5 = sum([element[1][int(element[0] * rightSkip / downSkip) % len(element[1])] == '#' for element in [(xindex, ylist) for xindex, ylist in enumerate([[i for i in j if not i == '\n'] for j in lines])] if element[0] % downSkip == 0])

print(trees1*trees2*trees3*trees4*trees5)