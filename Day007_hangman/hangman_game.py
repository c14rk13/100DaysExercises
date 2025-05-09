import random
import hangman_words
from hangman_art import logo, stages


print(logo)

#Randomly choose a word from word_list and assign to variable called chosen_word. then print it
chosen_word = random.choice(hangman_words.word_list)

#Create an empty string called placeholder. For each letter int he chosen_word, add a _ to placeholder
placeholder = ""
guessedLetters = []
for idx in range(0,len(chosen_word)):
    placeholder += "_"
print(placeholder)

isComplete = False
maxGuesses = 6
livesRemaining = maxGuesses


while not isComplete and livesRemaining > 0:

    print(f'Word to guess: {placeholder}')

    placeholder = ""

    #Ask the user to guess a letter and assign to a variable called guess. Make guess lowercase
    guess = input("Guess a letter: ").lower()

    #Check if the user already guessed the letter previously
    if guess in guessedLetters:
        print(f"You've already guessed {guess}")

    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.
    for idx in range(0,len(chosen_word)):
        char = chosen_word[idx]
        if char in guessedLetters:
            placeholder += char
        elif guess == char:
            placeholder += char
            guessedLetters.append(char)
        else:
            placeholder += "_"

    if not guess in guessedLetters:
        livesRemaining -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    else:
        print(placeholder)

    if not "_" in placeholder:
        isComplete = True

    # Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
    print(stages[livesRemaining])
    if livesRemaining > 0:
        print(f"******************** {livesRemaining}/{maxGuesses} lives left ********************")

if isComplete:
    print("You WIN !!!")
else:
    print(f"It was -- {chosen_word} -- You LOSE :(")

