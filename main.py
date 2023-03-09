# Imports
from board import *

# Messages
success = "Correct match! +{} points! Player {} has {} total points."

# Methods
def getPeople():
    while True:
        try:
            pl = int(input("Please insert the number of players: "))
        except ValueError:
            print(error)
            continue
        else:
            break
    return pl


def getDifficulty():
    while True:
        try:
            diff = int(input(
                "Choose the level of difficulty: Easy (1), Moderate (2), Challenging (3): "))
        except ValueError:
            print(error)
            continue
        if diff not in (1, 2, 3):
            print(error)
        else:
            if diff == 1:
                y = 4
            elif diff == 2:
                y = 10
            else:
                y = 13
            break
    return y, diff


def getWinner(points):
    winner = 0
    for i in range(1, len(points)):
        if (points[i] > points[winner]):
            winner = i
    return winner


# Main
print("Welcome to Matching Game")

# Get starting input
pl = getPeople()
y, diff = getDifficulty()

# Set default values
x = 4
player = 0
points = ([0] * pl)

# Creating boards
playingBoard = board(x, y, 0)
tempBoard = board(x, y, 0)
hiddenBoard = board(x, y, diff)

# While the board is not totaly flipped
while not hiddenBoard.isOver():
    # Print board
    # tempBoard.print()
    playingBoard.print()

    # Choose 1st card
    x1, y1 = hiddenBoard.getCard(player, 1)
    # Show chosen card
    tempBoard.set(x1, y1, hiddenBoard.get(x1, y1))
    tempBoard.print()

    # Choose 2nd card
    x2, y2 = hiddenBoard.getCard(player, 2)
    # Show chosen card
    tempBoard.set(x2, y2, hiddenBoard.get(x2, y2))
    tempBoard.print()

    # If they match
    if (hiddenBoard.get(x1, y1).symbol == hiddenBoard.get(x2, y2).symbol):
        # Increase player's points
        points[player] += hiddenBoard.get(x1, y1).worth

        # Print success message
        print(success.format(hiddenBoard.get(
            x1, y1).worth, (player+1), points[player]))

        # Replace boards
        playingBoard = tempBoard

        # Flip cards
        hiddenBoard.get(x1, y1).cond = True
        hiddenBoard.get(x2, y2).cond = True

        # Next player plays
        if not (hiddenBoard.get(x1, y1).symbol == "J"):
            player = playingBoard.next(player, pl, x1, y1)

    # Else, if player has 2nd chance
    elif ((hiddenBoard.get(x1, y1).symbol == "Q") and (hiddenBoard.get(x2, y2).symbol == "K")) or ((hiddenBoard.get(x1, y1).symbol == "K") and (hiddenBoard.get(x2, y2).symbol == "Q")):
        # Choose 3rd card
        x3, y3 = hiddenBoard.getCard(player, 3)
        # Show chosen card
        tempBoard.set(x3, y3, hiddenBoard.get(x3, y3))
        tempBoard.print()

        # If 1st and 3rd card match
        if (hiddenBoard.get(x1, y1).symbol == hiddenBoard.get(x3, y3).symbol):
            # Increase player's points
            points[player] += hiddenBoard.get(x1, y1).worth

            # Print success message
            print(success.format(hiddenBoard.get(
                x1, y1).worth, (player+1), points[player]))

            # Replace boards
            playingBoard = tempBoard

            # Flip cards
            tempBoard.get(x2, y2).desc = "X"
            hiddenBoard.get(x1, y1).cond = True
            hiddenBoard.get(x3, y3).cond = True

            # Next player plays
            player = playingBoard.next(player, pl, x3, y3)

        # Else, if 2nd and 3rd card match
        elif (hiddenBoard.get(x2, y2).symbol == hiddenBoard.get(x3, y3).symbol):
            # Increase player's points
            points[player] += hiddenBoard.get(x2, y2).worth

            # Print success message
            print(success.format(hiddenBoard.get(
                x2, y2).worth, (player+1), points[player]))

            # Replace boards
            playingBoard = tempBoard

            # Flip cards
            tempBoard.get(x1, y1).desc = "X"
            hiddenBoard.get(x2, y2).cond = True
            hiddenBoard.get(x3, y3).cond = True

            # Next player plays
            player = playingBoard.next(player, pl, x3, y3)

        # Else
        else:
            # Next player plays
            player = (player+1) % pl

            # Replace boards
            tempBoard = hiddenBoard

    # Else, if they have same series
    elif (hiddenBoard.get(x1, y1).series == hiddenBoard.get(x2, y2).series):
        # Increase player's points
        points[player] += (hiddenBoard.get(x1, y1).worth +
                           hiddenBoard.get(x2, y2).worth)

        # Print success message
        print(success.format(hiddenBoard.get(
            x1, y1).worth, player, points[player]))

        # Replace boards
        playingBoard = tempBoard

        # Flip cards
        hiddenBoard.get(x1, y1).cond = True
        hiddenBoard.get(x2, y2).cond = True

        # Next player plays
        player = (player+1) % pl

    # Else
    else:
        # Next player plays
        player = (player+1) % pl

        # Replace boards
        tempBoard = hiddenBoard

# When game ends
# Find the winner
winner = getWinner(points)

# Print winning message
print("Congratulations! Players {} won with {} points!".format(
    (winner+1), points[winner]))
