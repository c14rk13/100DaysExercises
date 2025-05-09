from tkinter import *

def convert_mi_to_km():
    value_miles = float(input_mi.get())
    value_km = value_miles * 1.609344
    label_convert.config(text=f"{value_km: .2f}")

window = Tk()
window.minsize(width=500, height= 300)
window.config(padx=50, pady=50)
window.title("Mile to Km Converter")


input_mi = Entry(width=5, font=("Arial", 20, "bold"))
input_mi.grid(column=1, row=0)

label_mi = Label(text="Miles", font=("Arial", 20, "bold"))
label_mi.grid(column=2, row=0)

label_equals = Label(text="is equal to", font=("Arial", 20, "bold"))
label_equals.grid(column=0, row=1)

label_convert = Label(text="0", font=("Arial", 20, "bold"))
label_convert.grid(column=1, row=1)

label_km = Label(text="Km", font=("Arial", 20, "bold"))
label_km.grid(column=2, row=1)

button_calc = Button(text="Calculate", font=("Arial", 20, "bold"), command=convert_mi_to_km)
button_calc.grid(column=1, row=2)

window.mainloop()