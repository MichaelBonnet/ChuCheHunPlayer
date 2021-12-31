import BoardPosition
import Player

class GameBoard:
    
    # Non-constructor-initialized variables
    BoardPositions = []

    # Adds a board position to the BoardPositions[] list.
    def addBoardPosition(self, BoardPosition):
        self.BoardPositions.append(BoardPosition)
    
    # Constructor, taking Players as arguments to populate the two players
    # and then creating the 9 board positions and establishing connectivity between positions
    def __init__(self, Player1, Player2):
        self.Player1 = Player1
        self.Player2 = Player2
        
        self.addBoardPosition(BoardPosition("A1", "Player 2")) # 0
        self.addBoardPosition(BoardPosition("A2", "Player 2")) # 1
        self.addBoardPosition(BoardPosition("A3", "Player 2")) # 2
        self.addBoardPosition(BoardPosition("B1", " Empty  ")) # 3
        self.addBoardPosition(BoardPosition("B2", " Empty  ")) # 4
        self.addBoardPosition(BoardPosition("B3", " Empty  ")) # 5
        self.addBoardPosition(BoardPosition("C1", "Player 1")) # 6
        self.addBoardPosition(BoardPosition("C2", "Player 1")) # 7
        self.addBoardPosition(BoardPosition("C3", "Player 1")) # 8

        # A1 - A2 - A3   # 0 - 1 - 2
        # | \  |  / |    # | \ | / |
        # B1 - B2 - B3   # 3 - 4 - 5
        # | /  |  \ |    # | / | \ |
        # C1 - C2 - C3   # 6 - 7 - 8

        BoardPosition[0].addNeighbors(BoardPosition[4], BoardPosition[1], BoardPosition[3])
        BoardPosition[1].addNeighbors(BoardPosition[4], BoardPosition[2])
        BoardPosition[2].addNeighbors(BoardPosition[4], BoardPosition[5])
        BoardPosition[3].addNeighbors(BoardPosition[4], BoardPosition[6], BoardPosition[7])
        BoardPosition[5].addNeighbors(BoardPosition[4], BoardPosition[7], BoardPosition[8])
        BoardPosition[6].addNeighbors(BoardPosition[4], BoardPosition[7])
        BoardPosition[7].addNeighbors(BoardPosition[4], BoardPosition[8])
        BoardPosition[8].addNeighbors(BoardPosition[4])

        Player1.updateOccupiedBoardPositions(self.BoardPositions)
        Player2.updateOccupiedBoardPositions(self.BoardPositions)

    # Print a visual representation of the current state of the board
    def printBoard(self):

        boardString = \
            "******************************************************\n\
            * [ {} ] ----- [ {} ] ----- [ {} ] *\n\
            *   |   \        |         /  |    *\n\
            *   |    \       |        /   |    *\n\
            *   |     \      |       /    |    *\n\
            *   |      \     |      /     |    *\n\
            *   |       \    |     /      |    *\n\
            * [ {} ] ----- [ {} ] ----- [ {} ] *\n\
            *   |       /    |     \      |    *\n\
            *   |      /     |      \     |    *\n\
            *   |     /      |       \    |    *\n\
            *   |    /       |        \   |    *\n\
            *   |   /        |         \  |    *\n\
            * [ {} ] ----- [ {} ] ----- [ {} ] *"
            
        print( boardString.format(
            self.BoardPositions[0].state,
            self.BoardPositions[1].state,
            self.BoardPositions[2].state,
            self.BoardPositions[3].state,
            self.BoardPositions[4].state,
            self.BoardPositions[5].state,
            self.BoardPositions[6].state,
            self.BoardPositions[7].state,
            self.BoardPositions[8].state ))

    # Move a player's piece from its current position to a new position
    def movePiece(self, Player, StartBoardPosition, EndBoardPosition):
        
        # Check for connectivity between neighbors
        if (StartBoardPosition.isNeighbor(EndBoardPosition)) and (EndBoardPosition.isNeighbor(StartBoardPosition)):

            # Check for empty ending position and that the player owns the piece to be moved
            if (EndBoardPosition.state == " Empty  ") and (StartBoardPosition.state == Player.name):
                
                StartBoardPosition.changeState(" Empty  ")   # Clear out the now-vacant position
                EndBoardPosition.changeState(Player.name)    # Update the now-occupied position
                Player.updateOccupiedBoardPositions(self.BoardPositions)

                self.printBoard()  # Print new board state

                return 1  # For error catching/game flow
            
            elif not (EndBoardPosition.state == " Empty  "):     # If the end position is invalid, report that
                print("End Position not empty! Try again.")
                return 0  # For error catching/game flow
            elif not (StartBoardPosition.state == Player.name):
                print("You do not own this piece! Try again.")
                return 0  # For error catching/game flow
        else:
            print("Chosen positions are not neighbors! Try again.")
            return 0  # For error catching/game flow

    # Check if the game is over, aka someone has no legal moves to make
    # Returns boolean True  for game over
    # Returns boolean False for game active
    def isGameOver(self):

        if ( self.Player1.hasLost() | self.Player2.hasLost() ):
            return True
        else:
            return False
