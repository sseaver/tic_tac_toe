game_matrix = [["_", "_", "_"],
               ["_", "_", "_"],
               ["_", "_", "_"]]

win_conditions_x = ["X", "X", "X"]
win_conditions_o = ["O", "O", "O"]
valid_input = ["0", "1", "2"]


def game_over():
    column_zero = [row[0] for row in game_matrix]
    column_one = [row[1] for row in game_matrix]
    column_two = [row[2] for row in game_matrix]
    columns = [column_zero, column_one, column_two]
    diagonal_up = [game_matrix[2][0], game_matrix[1][1], game_matrix[0][2]]
    diagonal_down = [game_matrix[0][0], game_matrix[1][1], game_matrix[2][2]]
    diagonal_wins = [diagonal_up, diagonal_down]
    for row in game_matrix:
        if row == win_conditions_o or row == win_conditions_x:
            print ("Congrats! You win!")
            return True
    for column in columns:
        if column == win_conditions_o or column == win_conditions_x:
            print ("Congrats! You win!")
            return True
    for diagonal in diagonal_wins:
        if diagonal == win_conditions_o or diagonal == win_conditions_x:
            print ("Congrats! You win!")
            return True


def move(game_matrix, player):
    print ("Pick a coordinate to place your {}".format(player))
    x_input = input("Row: ")
    y_input = input("Column: ")
    if x_input not in valid_input:
        print ("Invalid response")
        move(game_matrix, player)
    elif y_input not in valid_input:
        print ("Invalid response")
        move(game_matrix, player)
    elif game_matrix[int(x_input)][int(y_input)] != "_":
        print ("You can't go there!")
        move(game_matrix, player)
    else:
        game_matrix[int(x_input)][int(y_input)] = player



def draw_board(game_matrix):

    print ("   0     1     2 ")
    print ("0  {}  |  {}  |  {}".format(game_matrix[0][0], game_matrix[0][1], game_matrix[0][2]))
    print ("  ----+-----+----")
    print ("1  {}  |  {}  |  {} ".format(game_matrix[1][0], game_matrix[1][1], game_matrix[1][2]))
    print ("  ----+-----+----")
    print ("2  {}  |  {}  |  {} ".format(game_matrix[2][0], game_matrix[2][1], game_matrix[2][2]))

draw_board(game_matrix)
print ("X goes first!")

while True:
    move(game_matrix, "X")
    draw_board(game_matrix)
    if game_over():
        break
    move(game_matrix, "O")
    draw_board(game_matrix)
    if game_over():
        break
