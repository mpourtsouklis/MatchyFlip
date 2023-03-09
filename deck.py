# Imports
import random
from card import *


class deck:
    # Constructor
    def __init__(self, diff):
        self.cards = []
        self.build(diff)

    # Methods
    def build(self, diff):
        if diff == 1:
            symbolList = ["10", "J", "Q", "K"]
        elif diff == 2:
            symbolList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        else:
            symbolList = ["1", "2", "3", "4", "5", "6",
                          "7", "8", "9", "10", "J", "Q", "K"]
        for s in ["♥", "♣", "♦", "♠"]:
            for v in symbolList:
                self.cards.append(card(v, s, (v+s), getValue(v), False))

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

# Extra methods
def getValue(x):
    if x == "A":
        return 1
    elif (x == "J") or (x == "Q") or (x == "K"):
        return 10
    else:
        return int(x)
