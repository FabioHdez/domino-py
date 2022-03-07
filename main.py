import random

def main():
    # create pieces
    pieces = createPieces()

    # shuffle them
    random.shuffle(pieces)

    # Get input to get num of players (2 or 4)
    playerNum = int(input("Please enter the number of players (2 or 4): "))

    # Create players
    players = []
    for player in range(playerNum):
        name = input(f"Enter player {player+1}'s name: ")
        players.append(Player(name, pieces[:10]))
        del pieces[:10]

    # ACTUAL GAME
    table = []
    end = False

    # Check if the table is empty so that the first player can start the game
    if not table:
        print(f"{players[0].name} - pieces: ")
        print(players[0].pieces)
        choice = int(input(f"{players[0].name} - Choose a starting piece: ")) -1
        table.append(players[0].pieces[choice])
        players[0].pieces.pop(choice)
        players.insert(len(players),players.pop(0))
        print('-------------------------------------------------------')

    while(end == False):
        tableStatus = len(table)
        for player in range(playerNum):
            print(f"TABLE: \n {table} \n")
            print(f"{players[player].name} - pieces: ")
            print(players[player].pieces)
            players[player].play(table)
            print('------------------------------------------------------- \n')

        if tableStatus == len(table):
            end = True

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

class Player:
    def __init__(self, name, pieces):
        self.name = name
        self.pieces = pieces
    # checks if player can play. returns true or false
    def check(self,table):
        left = table[0][0]
        right = table[-1][-1]
        for piece in self.pieces:
            for num in piece:
                if num == left or num == right:
                    return True
        return False
    def play(self,table):
        left = table[0][0]
        right = table[-1][-1]
        if(self.check(table)):
            choice = int(input(f"{self.name} - Choose piece: ")) -1
            table.append(self.pieces[choice])
            self.pieces.pop(choice)

if __name__ == '__main__':
    main()
