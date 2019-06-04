import random

def roshambo():
    game_list = ["rock", "paper", "scissors"]
    game_choice = random.choice(game_list)

    your_choice = input("To play Roshambo type rock, paper, or scissors: ")

    if game_choice == "rock" and your_choice == "rock":
        print("Game is a tie, try again.")
    elif game_choice == "rock" and your_choice == "paper":
        print("You win, paper covers rock.")
    elif game_choice == "rock" and your_choice == "scissors":
        print("You lose, rock crushes scissors.")
    elif game_choice == "paper" and your_choice == "paper":
        print("Game is a tie, try again.")
    elif game_choice == "paper" and your_choice == "rock":
        print("You lose, paper covers rock.")
    elif game_choice == "paper" and your_choice == "scissors":
        print("You win, scissors cut paper.")
    elif game_choice == "sissors" and your_choice == "scissors":
        print("Game is a tie, try again.")
    elif game_choice == "scissors" and your_choice == "rock":
        print("You win, rock crushes scissors.")
    elif game_choice == "scissors" and your_choice == "paper":
        print("You lose, scissors cut paper.")
    else:
        print("You did not type rock, paper, or scissors. Try again.")
    
roshambo()
