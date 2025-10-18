from tkinter import *

window = Tk()
window.title("First GUI using tkinter")
window.minsize(500,300)

my_label = Label(text="I am a label.", font=("Aerial", 12, "bold"))
# my_label.pack()
# my_label.pack(side="left")
# my_label.pack(side="bottom")
my_label.pack(expand=True)

my_label["text"] = "New text"
my_label.config(text="New Text")

input = Entry(width=10)
input.pack()

def button_clicked():
    a = 0
    my_label.config(text=f"Text: {input.get()}")

button = Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()