def greet():
    print("Greetings earthling!")
    print("We come in peace")
    print("... mostly")

greet()


def life_in_weeks(current_age):
    remaining_life = (90 - current_age) * 52
    print(f"You have {remaining_life} weeks left.")

life_in_weeks(44)

def greet_with(name, location):
    print(f"Hello {name}! How is it like in {location}?")

greet_with("person","oblivion")
greet_with(location="somewhere",name="someone")



# Love Calculator
# # 💪 This is a difficult challenge! 💪
# # You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:
# # 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# # 2. Then check for the number of times the letters in the word LOVE occurs.
# # 3. Then combine these numbers to make a 2 digit number and print it out.
# # e.g.
# # name1 = "Angela Yu" name2 = "Jack Bauer"
# # T occurs 0 times
# # R occurs 1 time
# # U occurs 2 times
# # E occurs 2 times
# # Total = 5
#
# L occurs 1 time
# # O occurs 0 times
# # V occurs 0 times
# # E occurs 2 times
# # Total = 3
#
# # Love Score = 53
#
# # Example Input
# # calculate_love_score("Kanye West", "Kim Kardashian")
# # Example Output
# # 42
def calculate_love_score(name1, name2):
    combined_name = (name1 + name2).lower()
    love_score = 0
    love_score_str = ""

    for char in combined_name:
        if char == "t":
            love_score += 1
        if char == "r":
            love_score += 1
        if char == "u":
            love_score += 1
        if char == "e":
            love_score += 1

        love_score_str = str(love_score)

    love_score = 0
    for char in combined_name:
        if char == "l":
            love_score += 1
        if char == "o":
            love_score += 1
        if char == "v":
            love_score += 1
        if char == "e":
            love_score += 1

    love_score_str += str(love_score)
    print(love_score_str)


calculate_love_score("Cinderella", "Prince Charming")