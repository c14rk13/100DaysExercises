import tkinter

window = tkinter.Tk()
window.title("Some GUI Program")
window.minsize(width=500, height= 500)
# add padding to the window
window.config(padx=100, pady=200)


def button_clicked():
    print("I got clicked")
    my_label.config(text=f"Button clicked - {my_input.get()}")


#Label
my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0) #relative to other widgets, so (column=5, row=5) still shows top left
#my_label.pack() # Cannot use both pack() and grid() on same program
my_label.config(padx=50, pady=50)
my_label["text"] = "New Text"
my_label.config(text="Newer Text")

#Button
top_button = tkinter.Button(text="click me", command=button_clicked)
#button.pack()
top_button.grid(column=2, row=0)
top_button.config(padx=50, pady=50)


#Button
button = tkinter.Button(text="no, click me", command=button_clicked)
#button.pack()
button.grid(column=1, row=1)
button.config(padx=50, pady=50)


#Entry/Input field
my_input = tkinter.Entry(width=10)
my_input.grid(column=3, row=2)
#my_input.pack()
#my_input.config(padx=50, pady=50)






window.mainloop()