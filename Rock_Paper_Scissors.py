import random


moves = ["rock", "paper", "scissors"]
computer_choice = random.choice(moves)

guess = input("Enter your guess: ")

if guess == computer_choice:
    print("You win!")

else:
    print("You lose!")

