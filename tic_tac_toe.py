
game_matrix = [["_", "_", "_"],
               ["_", "_", "_"],
               ["_", "_", "_"]]

win_conditions_x = ["X", "X", "X"]
win_conditions_o = ["O", "O", "O"]

def winning():
    column_zero = [row[0] for row in game_matrix]
    column_one = [row[1] for row in game_matrix]
    column_two = [row[2] for row in game_matrix]

    if column_zero == win_conditions_x or column_zero == win_conditions_o:
        print ("Congrats! You win!")
        return True
    elif column_one == win_conditions_x or column_one == win_conditions_o:
        print ("Congrats! You win!")
        return True
    elif column_two == win_conditions_x or column_two == win_conditions_o:
        print ("Congrats! You win!")
        return True
    else:
        return False

def x_move(row, column):
    game_matrix[row][column] = "X"

def o_move(row, column):
    game_matrix[row][column] = "O"

def draw_board(game_matrix):

    print ("   0     1     2 ")
    print ("0  {}  |  {}  |  {}".format(game_matrix[0][0], game_matrix[0][1], game_matrix[0][2]))
    print ("  ----+-----+----")
    print ("1  {}  |  {}  |  {} ".format(game_matrix[1][0], game_matrix[1][1], game_matrix[1][2]))
    print ("  ----+-----+----")
    print ("2  {}  |  {}  |  {} ".format(game_matrix[2][0], game_matrix[2][1], game_matrix[2][2]))

draw_board(game_matrix)
print ("X goes first!")
# valid_input = [0, 1, 2]
# valid answers and end of game ######
while True:
    print ("Pick a coordinate to place your 'X'")
    x_move(int(input("Row: ")), int(input("Column: ")))
    draw_board(game_matrix)
    if winning():
        break
    print ("Pick a coordinate to place your 'O'")
    o_move(int(input("Row: ")), int(input("Column: ")))
    draw_board(game_matrix)
    if winning():
        break
