#Rock, Paper, Scissors interactive game
#Last Modified: 16 Decemeber 2014
#Created By: Zehra Punjwani

#import random module
import random

#main function
def main():
    #intro message
    print("Let's play 'Rock, Paper, Scissors'!")
    #call the user's guess function
    userGuess = user_guess()
    #call the computer's number function
    compGuess = computer_number()
    #call the results function
    results(compGuess, userGuess)

#computer_number function
def computer_number():
    #get a random number in the range of 1 through 3
    num = random.randrange(1,4)
    if num == 1:
        print("Computer chooses rock")
    elif num == 2:
        print("Computer chooses paper")
    elif num == 3:
        print("Computer chooses scissors")
    return num

#user_guess function
def user_guess():
    #get the user's guess
    guess = raw_input("Choose rock, paper, or scissors by typing that word.")
    #while guess == 'paper' or guess == 'rock' or guess == 'scissors':
    #assign 1 to rock
    if guess == "rock":
        return 1
    #assign 2 to paper
    elif guess == "paper":
        return 2
    #assign 3 to scissors
    elif guess == "scissors":
        return 3
    else:
        print("That response is invalid.")
        user_guess()

def restart():
    answer = raw_input("Would you like to play again? Enter 'y' for yes or 'n' for no: ")
    if answer == 'y':
        main()
    elif answer == 'n':
        print("Goodbye!")
    else:
        print("Please enter only 'y' or 'n'!")
        restart()

def results(compGuess, userGuess):
    #find the difference in the two numbers
    difference = compGuess - userGuess
    if difference == 0:
        print("TIE!")
        restart()
    elif difference % 3 == 1:
        print("I'm sorry! You lost :(")
        restart()
    elif difference % 3 == 2:
        print("Congratulations! You won :)")
        restart()

main()
