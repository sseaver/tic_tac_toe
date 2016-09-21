
def winning():
    column_zero = [row[0] for row in game_matrix]
    column_one = [row[1] for row in game_matrix]
    column_two = [row[2] for row in game_matrix]
    if column_zero == ["X", "X", "X"]:
        return True
        print ("X has won the game!")
    elif column_zero == ["O", "O", "O"]:
        return True
        print ("O has won the game!")
    else:
        return False

    if column_one == ["X", "X", "X"]:
        return True
        print ("X has won the game!")
    elif column_one == ["O", "O", "O"]:
        return True
        print ("O has won the game!")
    else:
        return False

    if column_two == ["X", "X", "X"]:
        return True
        print ("X has won the game!")
    elif column_two == ["O", "O", "O"]:
        return True
        print ("O has won the game!")
    else:
        return False

    if game_matrix[0] == ["X", "X", "X"]:
        return True
        print ("X has won the game!")
    elif game_matrix[0] == ["O", "O", "O"]:
        return True
        print ("O has won the game!")
    else:
        return False

    if game_matrix[1] == ["X", "X", "X"]:
        return True
        print ("X has won the game!")
    elif game_matrix[1] == ["O", "O", "O"]:
        return True
        print ("O has won the game!")
    else:
        return False

    if game_matrix[2] == ["X", "X", "X"]:
        return True
        print ("X has won the game!")
    elif game_matrix[2] == ["O", "O", "O"]:
        return True
        print ("O has won the game!")
    else:
        return False

########################################################

game_over = winning()
draw_board(game_matrix)
print ("X goes first!")

while not game_over:
    print ("Pick a coordinate to place your 'X'")
    x_move(int(input("Row: ")), int(input("Column: ")))
    draw_board(game_matrix)
    game_over = winning()
    print ("Pick a coordinate to place your 'O'")
    o_move(int(input("Row: ")), int(input("Column: ")))
    draw_board(game_matrix)
    game_over = winning()
