from art import gavel_logo

print(gavel_logo)

def get_winner(bids):
    winner_name = ""
    winner_bid = 0

    for single_bid in bids:
        current_bid = single_bid["bid"]
        if current_bid > winner_bid:
            winner_name = single_bid["name"]
            winner_bid = current_bid

    print("\n" * 20)
    print(f"The winner is {winner_name} with a bid of ${winner_bid}")


bidders = []
keep_bidding = True

while keep_bidding:
    your_name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    more_bidders = input("Are there any bidders? Type 'yes' or 'no': ").lower()

    bidders.append({your_name: bid})
    if more_bidders == "yes":
        print("\n" * 20)
    else:
        keep_bidding = False

get_winner(bidders)
