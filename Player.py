import BoardPosition

class Player:

    occupiedBoardPositions = []
    turnPlayer = False
    
    def __init__(self, name):
        self.name = name

    def updateOccupiedBoardPositions(self, BoardPositions):

        tempPositions = []

        for position in BoardPositions:
            if position.state == self.name:
                tempPositions.append(position)

        self.occupiedBoardPositions = tempPositions

    # Check to see if the player has lost.
    # Returns boolean value True  if the player has lost,
    #         boolean value False if the player has not lost.
    def hasLost(self):

        trapped_pieces = 0

        for position in self.occupiedBoardPositions:
            if not position.hasLegalMoves():
                trapped_pieces += 1
        
        if trapped_pieces >= 3:
            return True
        else:
            return False
