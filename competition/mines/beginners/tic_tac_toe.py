letter = input()
row_1 = [x for x in input()]
row_2 = [x for x in input()]
row_3 = [x for x in input()]
grid = [row_1, row_2, row_3]

def check_win(row, col):
    grid[row][col] = letter
    if check_horizontal() or check_vertical() or check_diagonal():
        grid[row][col] = 'E'
        return True
    else:
        grid[row][col] = 'E'
        return False
    
def check_horizontal():
    if (grid[0][0] == grid[0][1] == grid[0][2] or
        grid[1][0] == grid[1][1] == grid[1][2] or
        grid[2][0] == grid[2][1] == grid[2][2]):
            return True
    return False

def check_vertical():
    if (grid[0][0] == grid[1][0] == grid[2][0] or
        grid[0][1] == grid[1][1] == grid[2][1] or
        grid[0][2] == grid[1][2] == grid[2][2]):
        return True
    return False

def check_diagonal():
    if (grid[0][0] == grid[1][1] == grid[2][2] or
        grid[0][2] == grid[1][1] == grid[2][0]):
        return True
    return False

for row in range(3):
    for col in range(3):
        if grid[row][col] == 'E':
            if check_win(row, col):
                print((row + 1), (col + 1))