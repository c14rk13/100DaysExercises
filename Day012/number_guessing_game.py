import random
from art import guess_number_logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    max_attempts = HARD_LEVEL_TURNS
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if level == 'easy':
        max_attempts = EASY_LEVEL_TURNS

    return max_attempts


def compare_guess(user_guess, num_to_guess, turns_remaining):

    if user_guess == num_to_guess:
        print(f"You got it! The answer was {num_to_guess}.")
    elif user_guess < num_to_guess:
        print("Too low.\nGuess again.")
        turns_remaining -= 1
    else:
        print("Too high.\nGuess again.")
        turns_remaining -= 1

    return turns_remaining


def guess_a_number():
    print(guess_number_logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Set the number to guess
    number_to_guess = random.randint(1, 100)

    remaining_attempts = set_difficulty()
    guess = -1

    while guess != number_to_guess:
        print(f"You have {remaining_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        remaining_attempts = compare_guess(guess, number_to_guess, remaining_attempts)

        if remaining_attempts == 0 and not win:
            print(f"You've run out of guesses. The number was {number_to_guess}.")
            return

guess_a_number()