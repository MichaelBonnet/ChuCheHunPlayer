class BoardPosition:

    neighbors = []
    # state = " Empty  "

    def __init__(self, name, state):
        self.name = name
        self.state = state

    def addNeighbors(self, newNeighbors):
        for newNeighbor in newNeighbors:
            if newNeighbor not in self.neighbors:
                self.neighbors.append(newNeighbor)
            if self not in newNeighbor.neighbors:
                newNeighbor.neighbors.append(self)

    def isNeighbor(self, neighbor):
        if neighbor in self.neighbors:
            return True
        else:
            return False

    def changeState(self, state):
        self.state = state

    def hasLegalMovies(self):

        legal_move_count = 0
        
        for neighbor in self.neighbors:
            if neighbor.state != " Empty  ":
                legal_move_count += 1

        if legal_move_count == 0:
            return False
        else:
            return True
