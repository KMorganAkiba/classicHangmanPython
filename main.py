import random
import math

puzzles = []
usersSelections = []
gameStatus = True
wrongGuess = 0 

#reads puzzle file 
file = open('puzzles.txt', 'r')
puzzles = file.readlines()
file.close()

#select a random puzzle from puzzles.txt to be the game puzzle and splits the stirng into list of characters
puzzleChoice = math.floor(random.random() * len(puzzles))
selectedPuzzle = puzzles[puzzleChoice].strip()
gamePuzzle = list(selectedPuzzle)

while gameStatus == True:
    puzzleLength = len(gamePuzzle)
    print(gamePuzzle)
    playerGuess = input('Select a letter to guess:')
    if playerGuess not in usersSelections:
        usersSelections.append(playerGuess)
        if playerGuess in gamePuzzle:
            gamePuzzle.remove(playerGuess)
            for i in range (puzzleLength):
                if playerGuess in gamePuzzle:
                    gamePuzzle.remove(playerGuess)
                    print(gamePuzzle)
            puzzleLength = len(gamePuzzle)
            if puzzleLength == 0:
                print("You win Game Over!")
                gameStatus = False
        else:
            wrongGuess +=1
            print ("Choose another letter!")
            if wrongGuess == 3:
                print('Game Over: You Lose!')
                gameStatus = False
    else:
        playerGuess = input('Letter has been chosen already, Choose again:')



