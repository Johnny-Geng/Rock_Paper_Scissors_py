# Johnny Geng, johnnyge@usc.edu

# Description:
# This program allows the user to play Rock, Paper, Scissors against the computer.

import random


# Name: displayMenu
# Input: none
# Output: None
# Side effect: print game rules
# Description: displays the game rules to the user
def displayMenu():
    print("Welcome! Let's play rock, paper, scissors.\nThe rules of the game are:\n"
           "Rock smashes scissors\nScissors cut paper\nPaper covers rock\n"
          "If both the choices are the same, it's a tie")


# Name: getComputerChoice
# Input: none
# Output: integer that is randomly chosen, a number between 0 to 2
# Side effect: none
# Description: generate computer's choice randomly
def getComputerChoice():
    computer = random.randint(0,2)
    return computer


# Name: getPlayerChoice
# Input: none
# Output: integer that represents the player's choice
# Side effect: none
# Description: Asks the user for their choice: 0 for rock, 1 for paper, or 2 for scissors.
def getPlayerChoice():
    player = input("Please choose (0) for rock, (1) for paper or (2) for scissors: ")
    while player != "0" and player != "1" and player != "2":
        player = input("Please choose (0) for rock, (1) for paper or (2) for scissors: ")
    return int(player)


# Name: playRound
# Input: two integers (one representing computer's choice and the other representing the player's)
# Output: integer
# Side effect: none
# Description: To figure out who (user / computer) won this game; or if they tied.
def playRound(computerChoice, playerChoice):
    if playerChoice == computerChoice:
        return 0
    elif playerChoice == 0:
        if computerChoice == 1:
            return -1
        else:
            return 1
    elif playerChoice == 1:
        if computerChoice == 0:
            return 1
        else:
            return -1
    else:
        if computerChoice == 0:
            return -1
        else:
            return 1


# Name: continueGame
# Input: none
# Output: boolean
# Side effect: none
# Description: Ask the user to continue, and then return True (Y) or False (N) accordingly.
def continueGame():
    question = input("Do you want to continue playing (y or n)?\n>")
    while question.lower() != "y" and question.lower() != "n":
        question = input("Do you want to continue playing (y or n)?\n>")
    if question.lower() == "y":
        return True
    else:
        return False


# Name: main
# Input: none
# Output: none
# Side effect: display all the final results
# Description: logic run of the game(s).
def main():
    computerWin = 0
    playerWin = 0
    tied = 0
    round = 0
    x = True
    while x:
        displayMenu()
        a = getComputerChoice()
        b = getPlayerChoice()
        result = playRound(a,b)
        if result == 0:
            tied += 1
            winner = "You tied with the computer."
        elif result == 1:
            playerWin += 1
            winner = "You win!"
        else:
            computerWin += 1
            winner = "Computer wins!"
        round += 1
        if a == 0:
            computer = "Rock"
            if b == 0:
                player = "Rock"
                c = "The choices are the same."
            elif b == 1:
                player = "Paper"
                c = "Paper covers Rock."
            else:
                player = "Scissors"
                c = "Rock smashes Scissors."
        elif a == 1:
            computer = "Paper"
            if b == 1:
                player = "Paper"
                c = "The choices are the same."
            elif b == 0:
                player = "Rock"
                c = "Paper covers Rock."
            else:
                player = "Scissors"
                c = "Scissors cut Paper."
        else:
            computer = "Scissors"
            if b == 0:
                player = "Rock"
                c = "Rock smashes Scissors."
            elif b == 1:
                player = "Paper"
                c = "Scissors cut Paper."
            else:
                player = "Scissors"
                c = "The choices are the same."
        print("You chose " + player)
        print("The computer chose " + computer)
        print(c, end=" ")
        print(winner)
        x = continueGame()
    print("You won", playerWin, "game(s).")
    print("The computer won", computerWin, "game(s).")
    print("You tied with the computer", tied, "time(s).")
    print("\nThanks for playing!")


main()
