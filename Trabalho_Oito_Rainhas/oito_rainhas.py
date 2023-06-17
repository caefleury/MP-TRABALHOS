"""Program that checks if input (chess table) has 8 queens that cannot
attack each other"""

TABLE_INPUT_FORMAT = '00001000 01000000 00010000 00000010 00100000 00000001 00000100 10000000'
row_list = TABLE_INPUT_FORMAT.split()


def check_table(table):
    """Function that checks if table has valid size and valid queen count.
     Also checks horizontal validation """
    print(table)
    count = 0
    if len(table) != 8:
        return False
    for row in table:
        if len(row) != 8:
            return False
        count = 0
        for char in row:
            if char == '1':
                count += 1
        if count > 1:
            return False
    return True


def check_vertical(table):
    """ Returns True if there aren't two queens in same column"""
    for i in range(8):
        count = 0
        for row in table:
            if row[i] == '1':
                count += 1
        if count > 1:
            return False
    return True


def check_diagonal(table):
    """ Returns True if there aren't two queens in diagonal range"""
    queen_positions = []
    for row in range(8):
        for colunm in range(8):
            if table[row][colunm] == '1':
                queen_positions.append([row, colunm])
    print(queen_positions)
    for i, queenleft in enumerate(queen_positions):
        for queen_right in queen_positions[i+1:]:
            xdifference = queenleft[0] - queen_right[0]
            ydifference = queenleft[1] - queen_right[1]
            if xdifference in (ydifference, ydifference * -1):
                print([queenleft, queen_right])
                return False
    return True


def check_game(table):
    """
     Returns 1 if it's a solution to the queen problem
     Returns 0 if it's a solution to the queen problem
     Returns -1 if the input is not valid (not 8x8, not 8 queens)
    """
    if not check_table(table):
        return -1
    if check_vertical(table) and check_diagonal(table):
        return 1
    return 0