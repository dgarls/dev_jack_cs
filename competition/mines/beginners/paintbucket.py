def printGrid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            print(grid[row][col], end=' ')
        print()

firstInput = [int(x) for x in input().split()]

grid = []

for i in range(firstInput[0]):
    grid.append([int(x) for x in input().split()])

coords = firstInput[2:]
key = grid[coords[0]][coords[1]]

