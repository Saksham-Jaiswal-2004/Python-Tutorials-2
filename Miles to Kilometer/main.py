from tkinter import *

def miles_to_km():
    miles = float(entry.get())
    km = miles*1.609
    label3.config(text=f"{km}")

window = Tk()
window.title("Miles To Kilometer Converter")
window.minsize(width=300, height=300)
window.config(padx=100, pady=100)

entry = Entry(width=10)
entry.grid(row=1, column=2)

label1 = Label(text="Miles")
label1.grid(row=1, column=3)

label2 = Label(text="is equal to")
label2.grid(row=2, column=1)

label3 = Label(text="0")
label3.grid(row=2, column=2)

label4 = Label(text="Km")
label4.grid(row=2, column=3)

button = Button(text="Calculate", command=miles_to_km)
button.grid(row=3, column=2)

window.mainloop()