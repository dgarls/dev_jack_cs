row_1 = [x for x in input()]
row_2 = [x for x in input()]
grid = [row_1, row_2]
solved = [['1', '2'], ['3', '-']]

def move_dash():
    for row in range(2):
        for col in range(2):
            if grid[row][col] == '-':
                pos = row * 2 + col
    if pos == 0:
        grid[1][0], grid[0][0] = grid[0][0], grid[1][0]
    elif pos == 1:
        grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
    elif pos == 2:
        grid[1][0], grid[1][1] = grid[1][1], grid[1][0]
    elif pos == 3 and grid != solved:
        grid[1][1], grid[0][1] = grid[0][1], grid[1][1]

counter = 0
while grid != solved:
    move_dash()
    counter += 1
print(counter)

