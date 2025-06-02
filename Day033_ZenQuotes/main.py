from tkinter import *
import requests as req
from urllib3.exceptions import HTTPError


def get_quote():
    q_url = "https://zenquotes.io/api/random"
    try:
        response = req.get(url=q_url)
        response.raise_for_status()
        data = response.json()
        quote = data[0]["q"]
        author = data[0]["a"]
        canvas.itemconfig(quote_text, text=f"{quote} - {author}")
    except HTTPError:
        canvas.itemconfig(quote_text, text="Try again later..")



window = Tk()
window.title("Someone once said...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Zen Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="quote_icon.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()