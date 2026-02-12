import random

print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")

print("🎉 Congratulations! You guessed the number!")

