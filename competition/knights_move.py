letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
move = input()
row = letters.index(move[0])
col = int(move[1])

def isLegal(pos):
    if len(pos) > 2:
        return False
    row = letters.index(pos[0])
    col = int(pos[1])
    if row < 0 or col < 1 or row > 7 or col > 7:
        return False
    return True

changes = [2, 1, -1, -2]
for i in changes:
    if row - i < 0 or row - i > 7:
        continue
    letter = letters[row - i]
    if i % 2 == 0:
        first_move = letter + str(col - 1)
        second_move = letter + str(col + 1)
        moves = [first_move, second_move]
    else:
        first_move = letter + str(col - 2)
        second_move = letter + str(col + 2) 
        moves = [first_move, second_move]
    for move in moves:
        if isLegal(move):
            print(move)
