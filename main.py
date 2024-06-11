from tkinter import *


def miles_to_km():
    miles = float(user_input.get())
    km = miles * 1.609
    answer.config(text=km)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(300, 100)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="is equal to", font=("Arial", 13))
my_label.grid(column=0, row=2)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)

# Entry
user_input = Entry(width=10)
user_input.grid(column=1, row=1)

# Miles Label
miles_label = Label(text="Miles", font=("Arial", 13))
miles_label.grid(column=3, row=1)

# Km Label
km_label = Label(text="Km", font=("Arial", 13))
km_label.grid(column=3, row=2)

# answer Label
answer = Label(background="grey", width=10)
answer.grid(column=1, row=2)

window.mainloop()
