board = [
    [0, 0, 0, 0, 0, 0, 9, 0, 4],
    [0, 0, 0, 0, 3, 1, 0, 0, 0],
    [2, 9, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 3, 5, 6],
    [0, 6, 2, 0, 0, 0, 0, 8, 0],
    [0, 0, 5, 0, 8, 4, 0, 0, 0],
    [0, 0, 0, 3, 5, 7, 6, 0, 2],
    [0, 0, 0, 2, 0, 0, 0, 0, 8],
    [7, 0, 3, 0, 0, 0, 0, 0, 0],
]


def solve(bo):                      # Function is called again and again
    find = find_empty(bo)           # First num=0 found
    if not find:
        return True
    else:
        row, col = find             # If (row, col) exist, go ahead.

    for i in range(1, 10):
        if valid(bo, i, (row, col)):    # If number i valid:
            bo[row][col] = i            # Assign that number
            if solve(bo):               # This causes recursion?
                return True
            bo[row][col] = 0            # Without this some numbers are not checked at all.
    return False


def valid(bo, num, pos):                                # box, number to be checked [1-9], (row, col)
    # Check row
    for i in range(len(bo[0])):                         # len(bo[0]) = 9
        if bo[pos[0]][i] == num and pos[1] != i:        # if num in box[row][1-9] and col != [1-9]
            return False                                # INVALID: Number not correct

    # Check column
    for i in range(len(bo)):                            # len(bo) = 9
        if bo[i][pos[1]] == num and pos[0] != i:        # if num in box[1-9][col] and row != [1-9]
            return False                                # INVALID: Number not correct

    # Check box
    box_x = pos[1] // 3         # If actual pos[1] == 4 then box_x == 1: (3x3)box of index 1
    box_y = pos[0] // 3         # If actual pos[0] == 6 then box_y == 2: (3x3)box of index 2

    for i in range(3*box_y, 3 + 3*box_y):               # Check positions 2*3 to 2*3 + 3
        for j in range(3*box_x, 3 + 3*box_x):           # check positions 1*3 to 1*3 + 3
            if bo[i][j] == num and (i, j) != pos:       # if num in (3x3)box
                return False                            # INVALID: Number not correct

    return True                 # Yes! Number possible


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):                 # Finds first num = 0
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


print("Unsolved:")
print_board(board)
solve(board)
print("___________________\n\nSolved:")
print_board(board)
