import random

MIN_NUM = 1
MAX_NUM = 5
number_range = list(range(MIN_NUM, MAX_NUM + 1))

computer_choice = random.choice(number_range)

guess_input = input(f"Enter your guess between {MIN_NUM} and {MAX_NUM}: ")

try:
    guess = int(guess_input)

    if guess == computer_choice:
        print("You win! 🎉")
    else:
        print(f"You lose! 😢 The correct number was {computer_choice}.")

except ValueError:
    print("Invalid input. Please enter a valid number.")