import random

MIN_NUM = 0
MAX_NUM = 12

number_range = list(range(MIN_NUM, MAX_NUM + 1))

print("Welcome to the Math Test!")
print("")
print("How good are your times tables? Lets check ;-)")

computer_choice1 = random.choice(number_range)
computer_choice2 = random.choice(number_range)

Answer = computer_choice1 * computer_choice2

print(f"\nWhat is {computer_choice1} times {computer_choice2} ?")

guess = input("Answer : ")

try:
    user_answer = int(guess)

    if user_answer == Answer:
        print("correct!")
    else:
        print(f"wrong! The correct answer was {Answer}")

except ValueError:
    print("Invalid input. Please enter a number.")
