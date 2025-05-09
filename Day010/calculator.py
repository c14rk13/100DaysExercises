from art import calculator_logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# Assign each function to a symbol key in a dictionary
# Notes: You can assign a function into a variable and use that variable to call the function
#   ex. my_fav_operation = add
#       print(my_fav_operation(2,5))

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(calculator_logo)
    keep_calculating = True
    num1 = float(input("What's the first number? "))

    while keep_calculating:
        for symbol in operations:
            print(symbol)

        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))

        result = round(operations[operation](num1,num2),2) #ex: operations["*"](4,7)

        print(f"{num1} {operation} {num2} = {result}")


        continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation :").lower()
        if continue_calculation == "y":
            num1 = result
        elif continue_calculation == "n":
            keep_calculating = False
            calculator()
        else:
            return

calculator()