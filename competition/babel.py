def move(coord):
    row = coord[0]
    col = coord[1]
    global previous_move
    global letter
    global destination

    print("Previous move: ", previous_move)

    if tower[row-1][col] == letter and tower[row-1][col] != previous_move:
        previous_move = [row-1, col]
        move([row-1, col])
    elif tower[row][col-1] == letter and tower[row][col-1] != previous_move:
        previous_move = [row, col -1]
        move([row, col-1])
    elif tower[row + 1][col] == letter and tower[row + 1][col] != previous_move:
        previous_move = [row+1, col]
        move([row + 1, col])
    elif tower[row][col + 1] == letter and tower[row][col + 1] != previous_move:
        previous_move = [row, col + 1]
        move([row, col + 1])
    else:
        return False

    if coord == destination:
        return True
    

l = input().split()
rows = int(l[0])
cols = int(l[1])
tower = []


for i in range(rows):
    row = [x for x in input()]
    tower.append(row)

tests = int(input())

for test in range(tests):
    coords = input().split()
    start = [int(coords[0]), int(coords[1])]
    global previous_move
    global letter
    global destination
    previous_move = start
    letter = tower[int(coords[0])][int(coords[1])]
    destination = [int(coords[2]), int(coords[3])]
    can_move = move(start)
    if can_move:
        print(letter)
    else:
        print("N")

