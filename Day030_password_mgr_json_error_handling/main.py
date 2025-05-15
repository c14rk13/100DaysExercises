# JSON Functions:
# json.dump()
# json.load()
# json.update()
import json
from tkinter import *
from tkinter import messagebox
import pyperclip
import password_generator as p_gen

PASS_FILE = "data.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    # Clear password field
    # Generate a password
    # Copy the password to the clipboard

    passw = p_gen.generate_password()

    inp_pass.delete(0, END)
    inp_pass.insert(0, passw)

    pyperclip.copy(passw)

    # OR, use the ff Entry methods (works in Windows 11)
    #   inp_pass.clipboard_clear()
    #   inp_pass.clipboard_append(passw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    # Add validation
    website = inp_website.get().strip()
    uname = inp_uname.get().strip()
    passw = inp_pass.get().strip()
    new_data = {
        website: {
            "email": uname,
            "password": passw
        }}

    if website == "" or uname == "" or passw == "":
        # Show an alert here
        messagebox.showwarning("Warning: Incomplete Info", "All fields must be filled!")
        return

    # Ask user to confirm
    is_confirmed = messagebox.askokcancel(f"{website} - Proceed?", f"These are the details entered: \nEmail: {uname} "
                                          f"\nPassword: {passw} \nIs it ok to save?")
    if not is_confirmed:
        return

    # format entry to file
    entry = f"{website} | {uname} | {passw}\n"

    try:
        # Read form JSON file first
        with open(PASS_FILE, "r") as pass_file:
            data = json.load(pass_file)
            data.update(new_data)
    except FileNotFoundError:
        data = new_data
    finally:
        # Insert/Update to file
        with open(PASS_FILE, "w") as pass_file:
            json.dump(data, pass_file, indent=4)

    # Clear input fields (website and passw only):
    inp_website.delete(0, END)
    inp_pass.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search(search_txt):
    try:
        # Read form JSON file first
        with open(PASS_FILE, "r") as pass_file:
            data = json.load(pass_file)
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "No data found")
    else:
        # Add logic for search to be case-insensitive
        orig_keys = [key for key in data.keys()] # Website names in original case
        ci_keys = [key.lower() for key in orig_keys] # Websites in lower cases
        lc_search = search_txt.lower()

        # Find if website value in the list of keys (all lowercase)
        if lc_search in ci_keys:
            key = orig_keys[ci_keys.index(lc_search)] # Get the original case of the key
            email = data[key]["email"]
            passw = data[key]["password"]
            messagebox.showinfo(key,
                                f"Email: {email}\nPassword: {passw}")
        else:
            messagebox.showinfo(search_txt, "Password not found")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

lbl_website = Label(text="Website:")
lbl_website.grid(column=0, row=1)

inp_website = Entry(width=33)
inp_website.grid(column=1, row=1)

btn_search = Button(text="Search", width=15, command= lambda: search(inp_website.get().strip()))
btn_search.grid(column=2, row=1)

lbl_uname = Label(text="Email/Username:")
lbl_uname.grid(column=0, row=2)

inp_uname = Entry(width=52)
inp_uname.grid(column=1, row=2, columnspan=2)
inp_uname.insert(0, "my_email@gmail.com")

lbl_pass = Label(text="Password:")
lbl_pass.grid(column=0, row=3)

inp_pass = Entry(width=33)
inp_pass.grid(column=1, row=3)

btn_pass = Button(text="Generate Password", command=generate_pass)
btn_pass.grid(column=2, row=3)

bnt_add = Button(text="Add", width=44, command=add_pass)
bnt_add.grid(column=1, row=4, columnspan=2)

window.mainloop()