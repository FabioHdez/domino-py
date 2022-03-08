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
        print('------------------------------------------------------- \n')

    turn = 1
    while(end == False):
        tableStatus = len(table)
        for player in range(playerNum):
            print(f"TABLE: Turn: {turn} \n {table} \n")
            print(f"{players[player].name} - pieces: ")
            print(players[player].pieces)
            players[player].play(table)
            turn+=1
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

        # if there are playeable pieces in the player's hand allow user to pick
        if(self.check(table)):
            choice = int(input(f"{self.name} - Choose piece: ")) -1
            playeable_left = False
            playeable_right = False
            # Checks for all the possible ways that a player can play
            for num in self.pieces[choice]:
                if num == left and num == right:
                    playeable_left = True
                    playeable_right = True
                elif num == left:
                    playeable_left = True
                elif num == right:
                    playeable_right = True

            if playeable_left and playeable_right:
                side = input("Choose a side (left/right): ")
                print(f"Playin on the {side}")
                if side == "left":
                    playeable_right = False
                elif side == "right":
                    playeable_left = False

            if playeable_left:
                print("Playing on the left")
                table.insert(0,self.pieces[choice])
                self.pieces.pop(choice)
            elif playeable_right:
                print("Playing on the right")
                table.append(self.pieces[choice])
                self.pieces.pop(choice)
            else:
                print(f"{self.pieces[choice]} is not valid. Pick another piece")
                # recall play func in case that the player chooses wrong piece
                self.play(table)

if __name__ == '__main__':
    main()
