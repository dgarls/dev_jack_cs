def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=' ')
        print()

grid = []

line = input()
while line != '':
    try:
        grid.append(line)
        line = input()
    except EOFError as e:
        break

midLine = 0
longest = 0

#Find longest line/length of handle
for idx, line in enumerate(grid):
    if len(line) > longest:
        midLine = idx
        longest = len(line)

print(midLine)

numTongs = grid[midLine + 1].count('#')

tongCount = [1 for i in range(numTongs)]

print(*tongCount)