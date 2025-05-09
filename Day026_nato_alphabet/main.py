import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:
#   {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter:row.code for(index,row) in df.iterrows()}


# 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word/name: ")
word_char_list = [word.upper() for word in user_input]
phonetic_word = [phonetic_alphabet[char] for char in word_char_list]
print(phonetic_word)