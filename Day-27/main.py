import tkinter

window = tkinter.Tk()
window.title("First GUI using tkinter")
window.minsize(500,300)

my_label = tkinter.Label(text="I am a label.", font=("Aerial", 24, "bold"))
# my_label.pack()
# my_label.pack(side="left")
# my_label.pack(side="bottom")
my_label.pack(expand=True)

window.mainloop()