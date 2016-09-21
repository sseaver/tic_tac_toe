def draw_board():
    game_matrix = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    print ("  0     1    2 ")
    print ("0  {}  |  {}  | {}".format(game_matrix[0][0], game_matrix[0][1], game_matrix[0][2]))
    print ("  ----+-----+---")
    print ("1  {}  |  {}  | {} ".format(game_matrix[1][0], game_matrix[1][1], game_matrix[1][2]))
    print ("  ----+-----+---")
    print ("2  {}  |  {}  | {} ".format(game_matrix[2][0], game_matrix[2][1], game_matrix[2][2]))

draw_board()
