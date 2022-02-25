import random

def main():
    # create pieces
    pieces = resetPieces()
    p1Hand = selectPieces(pieces)

    p1 = Player("Fabio", pieces)

    # create players

def resetPieces():
    pieces = []
    for i in range(10):
        for j in range(10):
            pieces.append([i,j])
            for piece in pieces:
                if piece == [j,i] and j != i:
                    pieces.remove(piece)
    return pieces

# def selectPieces(pieces):
#     hand = []
#     while len(hand) < 10:
#         index = random.randint(0,len(pieces))
#
#     print(hand)




class Player:
    def __init__(self, name, pieces):
        self.name = name
        self.pieces = pieces
    def getPieces(self):
        print(self.pieces)



if __name__ == '__main__':
    main()
