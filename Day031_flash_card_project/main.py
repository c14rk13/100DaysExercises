import random
import time
from tkinter import *
from tkinter import messagebox

import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
CSV_FILE_MAIN = "./data/french_words.csv"
CSV_FILE_TO_LEARN = "./data/words_to_learn.csv"

flashcards = []
current_card = {}


# ============================ Functions ===============================
def completed():
    global flip_timer
    window.after_cancel(flip_timer)
    messagebox.showinfo(title="Congratulations!",
                        message="You have completed this deck of flashcards!")
    btn_wrong.config(state=DISABLED)
    btn_right.config(state=DISABLED)

    flashcard.itemconfig(title, fill="black", text="CONGRATULATIONS!")
    flashcard.itemconfig(word, fill="black", text="WELL DONE!")


def get_new_word():
    global current_card
    current_card = random.choice(flashcards)


def setup_flashcards():
    # Read list from csv, save to list of dictionaries
    try:
        translated_words = pandas.read_csv(CSV_FILE_TO_LEARN)
    except FileNotFoundError:
        translated_words = pandas.read_csv(CSV_FILE_MAIN)

    global flashcards
    flashcards = translated_words.to_dict(orient="records")


def check(is_correct):
    global flashcards

    if is_correct:
        # Remove word from flashcard list
        flashcards.remove(current_card)

        # Update the words_to_learn csv
        df_to_learn = pandas.DataFrame(flashcards)
        df_to_learn.to_csv(CSV_FILE_TO_LEARN, index=False)

    # Check for empty list
    if len(flashcards) == 0:
        completed()
    else:
        # Show front card with new word
        get_new_word()
        flash_front()



# ============================ UI ===============================
def flash_front():
    global flip_timer
    window.after_cancel(flip_timer)
    flashcard.itemconfig(card_img, image=img_card_front)
    flashcard.itemconfig(title, fill="black", text="French")
    flashcard.itemconfig(word, fill="black", text=current_card["French"])
    flip_timer = window.after(3000, flip_card)


def flip_card():
    flashcard.itemconfig(card_img, image=img_card_back)
    flashcard.itemconfig(title, fill="white", text="English")
    flashcard.itemconfig(word, fill="white", text=current_card["English"])

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
flip_timer = window.after(3000, flip_card)
flash_front()

window.mainloop()