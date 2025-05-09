from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine


def make_coffee():
    is_on = True
    coffee_machine = CoffeeMaker()
    coffee_menu = Menu()
    money = MoneyMachine()

    while is_on:
        #print(coffee_logo)
        user_choice = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()
        if user_choice == "off":
            #Turn off the Coffee Machine by entering “ off ” to the prompt.
            is_on = False
        elif user_choice == "report":
            #Print report.
            coffee_machine.report()
            money.report()
        else: #Get the drink ingredients
            drink = coffee_menu.find_drink(user_choice)
            if drink is None:
                print("That is not offered by this coffee machine")
            else:
                if coffee_machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                    coffee_machine.make_coffee(drink)

make_coffee()