line = [int(x) for x in input().split()]

numSquares = line[0]
square = line[1] - 1
magicNum = line[2]

numbers = [int(x) for x in input().split()]
magicNumLoc = numbers.index(magicNum)
numHops = 0
previousHops = []

while square > -1 and square < numSquares and square != magicNumLoc and square not in previousHops:
    previousHops.append(square)
    numHops += 1
    square += numbers[square]

if square < 0:
    print('left')
elif square >= numSquares:
    print('right')
elif square == magicNumLoc:
    print('magic')
else:
    print('cycle')
print(numHops)