from datetime import datetime
from art import report_logo, coffee_logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.00


# Check resources sufficient?
def check_resources(order_ingredients):
    # Compare available versus needed amounts:
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False

    return True



#Process coins.
def process_coins():
    # Initialize total_coins to 0 (indicating no coins successfully inserted)
    total_coins = 0

    # Prompt the user to insert coins
    print("Please insert coins")

    try:
        quarters = int(input("How many Quarters? "))
        dimes = int(input("How many Dimes? "))
        nickels = int(input("How many Nickels? "))
        pennies = int(input("How many Pennies? "))

        # Calculate the monetary value of the coins inserted
        #   quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
        total_coins = round((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01), 2)
    except ValueError:
        print("That is not a coin!")
    finally:
        return total_coins



# Check transaction successful?
def transact(drink_cost, total_coins):
    if total_coins > 0:
        # Check the coins against the value needed for the drink
        if total_coins < drink_cost:
            print("Sorry that's not enough money. Money refunded.")
            return False

        # Calculate change, if any
        if total_coins > drink_cost:
            change = total_coins - drink_cost
            formatted_change = "{:.2f}".format(change)
            print(f"“Here is ${formatted_change} in change.”")

        # Add money to coffee machine
        global money
        money += drink_cost

        return True

    else:
        print("You have not given enough coins (if you did, at all \N{unamused face}).")
        return False



# Make Coffee.
def make_coffee(order_ingredients):
    # Deduct ingredients from resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]



# Print report.
def print_report():
    print(report_logo)
    print("---------------------------------------------------------------")
    print(f"\tWater: \t\t{resources['water']} ml")
    print(f"\tMilk: \t\t{resources['milk']} ml")
    print(f"\tCoffee: \t{resources['coffee']} g")
    print(f"\tMoney: \t\t${money}")

    formatted_date_now = datetime.now().strftime('%A, %Y-%m-%d %H:%M:%S')
    print("---------------------------------------------------------------")
    print(f"Report Date and Time: {formatted_date_now}")
    print("---------------------------------------------------------------\n")



# Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
def coffee_maker():
    is_on = True
    while is_on:
        print(coffee_logo)
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice in ["espresso", "latte", "cappuccino"]:
            order_ingredients = MENU[user_choice]["ingredients"]
            if check_resources(order_ingredients):
                total_coins = process_coins()
                if transact(MENU[user_choice]["cost"], total_coins):
                    make_coffee(order_ingredients)
                    print(f"Here is your {user_choice} ☕. Enjoy!")

        elif user_choice == "off":
            #Turn off the Coffee Machine by entering “ off ” to the prompt.
            is_on = False
        elif user_choice == "report":
            #Print report.
            print_report()
        else:
            print("That is not offered by this coffee machine")



coffee_maker()