import GameBoard, Player

Player1 = Player("Player1")
Player2 = Player("Player2")

GameBoard = GameBoard(Player1, Player2)

GameBoard.printBoard()

Player1.turnPlayer = True

while not GameBoard.isGameOver():

    GameBoard.printBoard()

    if Player1.turnPlayer == True:
        start_board_position = input("\nPlayer 1, what position's piece do you want to move? ")
        end_board_position   = input("\nPlayer 2, what position do you want to move the piece to? ")
        GameBoard.movePiece(Player1, start_board_position, end_board_position)

        Player1.turnPlayer = False
        Player2.turnPlayer = True

    else:
        start_board_position = input("\nPlayer 2, what position's piece do you want to move? ")
        end_board_position   = input("\nPlayer 2, what position do you want to move the piece to? ")
        GameBoard.movePiece(Player1, start_board_position, end_board_position)

        Player2.turnPlayer = False
        Player1.turnPlayer = True

if GameBoard.isGameOver():

    winner = ""
    loser  = ""

    if Player1.hasLost():
        winner = Player2.name
        loser  = Player1.name
    else:
        winner = Player1.name
        loser  = Player2.name

    print("\nGame Over! {} cannot make any legal moves. {} is the winner!".format(loser, winner))



