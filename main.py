import random

def main():
    # create pieces
    pieces = createPieces()

    # shuffle them
    random.shuffle(pieces)

    # Get input to get num of players (2 or 4)
    playerNum = int(input("Please enter the number of players: "))

    # Create players
    players = []
    for player in range(playerNum):
        name = input(f"Enter player {player+1}'s name:")
        players.append(Player(name, pieces[:10]))
        del pieces[:10]

    # Select wether playing with people or COMP
    # ADD LATER


#Creates a list with all the pieces in the game
def createPieces():
    pieces = []
    for i in range(10):
        for j in range(10):
            pieces.append([i,j])
            for piece in pieces:
                if piece == [j,i] and j != i:
                    pieces.remove(piece)
    return pieces

# Gets the current pieces and selects the amount for each hand
# def selectPieces(pieces,handSize):




class Player:
    def __init__(self, name, pieces):
        self.name = name
        self.pieces = pieces
    def getPieces(self):
        print(self.pieces)



if __name__ == '__main__':
    main()
