import random
from art import blackjack_logo


def is_black_jack(cards):
    if 10 in cards and 11 in cards and sum(cards) == 21:
        return True
    else:
        return False


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # Returns 0 if it's a blackjack
    card_sum = sum(cards)

    if card_sum == 21 and len(cards) == 2:
        return 0 #Blackjack

    if card_sum > 21 and 11 in cards:
        # Replace 11 with 1
        cards.remove(11)
        cards.append(1)
        card_sum = sum(cards)

    return card_sum


def check_winner(player_score, dealer_score, keep_dealing):
    winner_message = ""
    if dealer_score == 0: #BlackJack
        winner_message = "Lose, opponent has Blackjack \N{face screaming in fear}"
    elif player_score == 0:
        winner_message = "You win with Blackjack \N{smiling face with sunglasses}"
    elif player_score > 21:
        winner_message = "You went over. You lose \N{loudly crying face}"
    elif dealer_score > 21:
        winner_message = "Opponent went over. You win \N{grinning face with smiling eyes}"
    elif player_score == dealer_score and not keep_dealing:
        winner_message = "It's a draw \N{upside-down face}"
    elif player_score > dealer_score > 16 and not keep_dealing:
        winner_message = "You win \N{grinning face}"
    elif dealer_score > 16 and player_score  < dealer_score and not keep_dealing:
        winner_message = "You lose \U0001F624"

    return winner_message


def play():
    print(blackjack_logo)

    player_cards = []
    dealer_cards = []
    winner_message = ""
    keep_dealing = True

    for _ in range(2):
        dealer_cards.append(deal_card())
        player_cards.append(deal_card())

    dealer_card = dealer_cards[0]

    while winner_message == "":
        player_card_sum = calculate_score(player_cards)
        dealer_card_sum = calculate_score(dealer_cards)

        winner_message = check_winner(player_card_sum, dealer_card_sum, keep_dealing)

        if winner_message == "":
            print(f"Your cards: {player_cards}, current score: {player_card_sum}")
            print(f"Computer's first card: {dealer_card}")

            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if choice == "y":
                player_cards.append(deal_card())
                dealer_cards.append(deal_card())
            else:
                keep_dealing = False
                while dealer_card_sum < 17 and not dealer_card_sum == 0: #add exception when it reaches 0 or blackjack
                    dealer_cards.append(deal_card())
                    dealer_card_sum = calculate_score(dealer_cards)
        else:
            print(f"Your final hand: {player_cards}, final score: {player_card_sum}")
            print(f"Computer's final hand: {dealer_cards}, final score: {dealer_card_sum}")
            print(winner_message)


keep_playing = input("Do you want to play Blackjack? Type 'y' for yes, 'n' for No: ").lower()
while keep_playing == "y":
    play()
    keep_playing = input("Do you want to play Blackjack? Type 'y' for yes, 'n' for No: ").lower()
    print("\n" * 25)
