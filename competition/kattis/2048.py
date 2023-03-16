def printGrid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            print(grid[row][col], end=' ')
        print()
    print()

directions = {
    0: 'left',
    1: 'up',
    2: 'right',
    3: 'down'
}

def move(row, direction):
    if direction == 'left':
        for i in range(3, 0, -1):
            if row[i] == 0:
                continue
            if row[i - 1] == 0:
                row[i - 1] = row[i]
                row[i] = 0

    elif direction == 'right':
        for i in range(3):
            if row[i] == 0:
                continue
            if row[i + 1] == 0:
                row[i + 1] = row[i]
                row[i] = 0

    return row



grid = [[0 for x in range(4)] for y in range(4)]
for i in range(4):
    grid[i] = [int(x) for x in input().split()]

direction = int(input())

if directions[direction] == 'left':
    for row in range(4):
        for col in range(3, 0, -1):
            num = grid[row][col]
            left = grid[row][col - 1]
            if num == 0:
                continue
            if left == num:
                grid[row][col - 1] = num * 2
                grid[row][col] = 0
            elif left == 0:
                grid[row][col - 1] = num
                grid[row][col] = 0
            printGrid(grid)
        grid[row] = move(grid[row], 'left')

elif directions[direction] == 'right':
    for row in range(4):
        for col in range(3):
            num = grid[row][col]
            right = grid[row][col + 1]
            if num == 0:
                continue
            if right == num:
                grid[row][col + 1] = num * 2
                grid[row][col] = 0
            elif right == 0:
                grid[row][col + 1] = num
                grid[row][col] = 0
            printGrid(grid)
        grid[row] = move(grid[row], 'right')


printGrid(grid)