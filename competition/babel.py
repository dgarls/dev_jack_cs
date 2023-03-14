l = input().split()
counter = 0
rows = int(l[0])
cols = int(l[1])
tower = []

def isValid(coord):
    global rows
    global cols
    if coord[0] < rows and coord[0] > -1 and coord[1] < cols and coord[1] > -1:
        return True
    
    return False

def move(coord):

    global destination

    if coord == destination:
        return True
    
    row = int(coord[0])
    col = int(coord[1])
    global previous_move
    global letter

    # Checking top
    if isValid([row-1, col]) and [row-1, col] not in previous_move and tower[row-1][col] == letter:
        previous_move.append([row, col])
        if move([row-1, col]):
            return True

    # Checking bottom
    if isValid([row + 1, col]) and [row + 1, col] not in previous_move and tower[row + 1][col] == letter:
        previous_move.append([row, col])
        if move([row + 1, col]):
            return True

    # Checking Left
    if isValid([row, col-1]) and [row, col-1] not in previous_move and tower[row][col-1] == letter:
        previous_move.append([row, col])
        if move([row, col - 1]):
            return True

    # Checking right
    if isValid([row, col+1]) and [row, col + 1] not in previous_move and tower[row][col + 1] == letter:
        previous_move.append([row, col])
        if move([row, col + 1]):
            return True
    
    return False


for i in range(rows):
    row = [x for x in input()]
    tower.append(row)

tests = int(input())

for test in range(tests):
    coords = input().split()
    start = [int(coords[0]), int(coords[1])]
    previous_move = start
    letter = tower[int(coords[0])][int(coords[1])]
    destination = [int(coords[2]), int(coords[3])]
    can_move = move(start)
    if can_move:
        print(letter)
    else:
        print("N")

