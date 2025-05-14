import random
import time
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
CSV_FILE = "./data/french_words.csv"

flashcard_words_fr = []
flashcard_words_en = []
current_word_idx = -1


# ============================ Functions ===============================
def get_new_word():
    global current_word_idx

    current_word_idx = random.randint(0, len(flashcard_words_fr)-1)
    # print(f"Current index: {current_word_idx}")
    # print(f"{flashcard_words_fr[current_word_idx]} - {flashcard_words_en[current_word_idx]}")
    # print(flashcard_words_fr)
    # print(flashcard_words_en)

def setup_flashcards():
    # Read list from csv, save to list of dictionaries
    translated_words = pandas.read_csv(CSV_FILE)

    global flashcard_words_fr, flashcard_words_en
    flashcard_words_fr = translated_words["French"].to_list()
    flashcard_words_en = translated_words["English"].to_list()


def check(is_correct):
    global flashcard_words_fr, flashcard_words_en

    if is_correct:
        # Remove word from flashcard list
        flashcard_words_fr.remove(flashcard_words_fr[current_word_idx])
        flashcard_words_en.remove(flashcard_words_en[current_word_idx])

        # TODO: Add error checking for empty list

    # Show front card with new word
    get_new_word()
    flash_front()


# ============================ UI ===============================
def flash_front():
    flashcard.itemconfig(card_img, image=img_card_front)
    flashcard.itemconfig(title, text="French")
    flashcard.itemconfig(word, text=flashcard_words_fr[current_word_idx])
    btn_wrong.config(state=DISABLED)
    btn_right.config(state=DISABLED)
    window.after(3000, flash_back)


def flash_back():
    flashcard.itemconfig(card_img, image=img_card_back)
    flashcard.itemconfig(title, text="English")
    flashcard.itemconfig(word, text=flashcard_words_en[current_word_idx])
    btn_wrong.config(state=NORMAL)
    btn_right.config(state=NORMAL)


window = Tk()
window.title("Flashy - French to English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images:
img_card_front = PhotoImage(file="./images/card_front.png")
img_card_back = PhotoImage(file="./images/card_back.png")
img_wrong = PhotoImage(file="./images/wrong.png")
img_right = PhotoImage(file="./images/right.png")

# Flashcard
flashcard = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_img = flashcard.create_image(400, 260, image=img_card_front)

# Text
title = flashcard.create_text(400, 130,text="Title", font=FONT_TITLE)
word = flashcard.create_text(400, 260,text="Title", font=FONT_WORD)

flashcard.grid(column=0, row=0, columnspan=2)

# Buttons
btn_wrong = Button(image=img_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command= lambda: check(False))
btn_right = Button(image=img_right, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0, command= lambda: check(True))
btn_wrong.grid(column=0, row=1)
btn_right.grid(column=1, row=1)


setup_flashcards()
get_new_word()
flash_front()

# window.after(3000, flash_back)



window.mainloop()