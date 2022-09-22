# This version of the game is much simpler than the other one I have uploaded on my GitHub.

import random

options = {1: "rock", 2: "paper", 3: "scissors"}


def winner_is(player_choice, computer_choice):
    winner = ""
    if (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
        winner = "Player"
    elif (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 3) or (player_choice == 3 and computer_choice == 1):
        winner = "Computer"
    elif player_choice == computer_choice:
        winner = "No one"
    return winner


def game(player_choice):
    computer_choice = random.choice(list(options.keys()))
    print(f"You chose: {options[player_choice]}")
    print(f"Computer chose: {options[computer_choice]}")
    winner = winner_is(player_choice, computer_choice)
    return f"{winner} wins!"


while True:
    print(game(player_choice=int(input("\nWelcome to Rock, Paper, Scissors! Type '1' for rock, '2' for paper and '3' for scissors:\n"))))
    play_again = input("\nDo you want to play another game? Type 'y' or 'n'.\n")
    if play_again == "n":
        print("Thank you for playing!")
        quit()