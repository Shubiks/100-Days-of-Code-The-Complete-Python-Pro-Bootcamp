from tkinter import *

window = Tk()

window.minsize(width=500, height=300)
window.title("GUI with tkinter")

my_label = Label(text="I am a Believer",font=("Arial",24,"bold"))
input = Entry()
input.grid(row=2,column=3)

def button_clicked():
    value = input.get()
    my_label["text"] = value


button = Button(text = "This is a Butoon" ,command=button_clicked)
button.grid(row=1,column=1)
new_button = Button(text="new_button")
new_button.grid(row=0,column=2)
# button["command"] = button_clicked
my_label.grid(row=0,column=0)
# my_label.config(text="New Text")

window.mainloop()