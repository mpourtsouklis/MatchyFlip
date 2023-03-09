# Imports
from deck import *
from tabulate import tabulate

# Messages
error = "You entered wrong input."
askRow = "Player {}, please insert the row  of the card no.{}: "
askCol = "Player {}, please insert the collumn of the card no.{}: "


class board:
    # Constructor
    def __init__(self, x, y, diff):
        self.board = [[] for k in range(x+1)]
        self.build(x, y, diff)

    # Methods
    def build(self, x, y, diff):
        if (diff == 0):
            for j in range(y+1):
                for i in range(x+1):
                    if (j == 0):
                        self.board[i].append(card(None, None, i, 0, True))
                    elif (i == 0):
                        self.board[i].append(card(None, None, j, 0, True))
                    else:
                        self.board[i].append(card(None, None, "X", 0, True))
        else:
            tempdeck = deck(diff)
            tempdeck.shuffle()
            for j in range(y+1):
                for i in range(x+1):
                    if (j == 0):
                        self.board[i].append(card(None, None, i, 0, True))
                    elif (i == 0):
                        self.board[i].append(card(None, None, j, 0, True))
                    else:
                        self.board[i].append(tempdeck.drawCard())

    def get(self, x, y):
        return self.board[x][y]

    def set(self, x, y, z):
        self.board[x][y] = z

    def next(self, player, players, x, y):
        if (self.board[x][y].symbol == "K"):
            return (player+2) % players
        else:
            return (player+1) % players

    def getCard(self, player, num):
        while True:
            try:
                row = int(input(askRow.format(player+1, num)))
                col = int(input(askCol.format(player+1, num)))
            except ValueError:
                print(error)
                continue
            if ((row not in (1, 2, 3, 4)) or (self.board[int(row)][col].cond)):
                print(error)
            else:
                return row, col

    def print(self):
        board = []
        
        for row in self.board:
            temp = []
            
            for index in row:
                temp.append(index.desc)
            
            board.append(temp)
        
        print(tabulate(board, tablefmt='fancy_grid'))

    def isOver(self):
        for i in self.board:
            for j in i:
                if (j.cond == False):
                    return False
        return True
