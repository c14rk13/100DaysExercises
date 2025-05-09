import random

from game_data import data
from art import higher_lower_logo, vs

def get_item():
    return random.choice(data)
    # Improve to return only unique


# Get 2 initial items to compare
# Ask user to guess/choose which has higher search count
# Compare the users guess against the correct answer



def compare(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "a"
    else:
        return "b"



def format_data(data):
    return f"{data['name']}, a/n {data['description']}, from {data['country']}"


def game():
    choice_a = get_item()
    choice_b = get_item()
    score = 0
    correct = True

    while correct:
        print(higher_lower_logo)
        print(f"Compare A: {format_data(choice_a)}")
        print(vs)
        print(f"Against B: {format_data(choice_b)}")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == compare(choice_a, choice_b):
            print(f"You're right! Current score: {score}")
            choice_a = choice_b
            choice_b = get_item()
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            correct = False

game()