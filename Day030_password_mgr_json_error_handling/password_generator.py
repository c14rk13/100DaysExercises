#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    your_password = []

    # Use list comprehension instead of for loop
    your_password += [random.choice(letters) for _ in range(nr_letters)]
    your_password += [random.choice(symbols) for _ in range(nr_symbols)]
    your_password += [random.choice(numbers) for _ in range(nr_numbers)]

    # Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    random.shuffle(your_password)

    return ''.join(your_password)