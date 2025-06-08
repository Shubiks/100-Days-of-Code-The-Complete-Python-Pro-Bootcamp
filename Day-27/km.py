from tkinter import *

window = Tk()
window.title("Converting miles to km")
window.minsize(width=300, height=200)

input = Entry()
input.grid(row=0,column=1)

label1 = Label(text="Miles")
label1.grid(row=0,column=2)

label2 = Label(text="is equal to")
label2.grid(row=1,column=0)
label3 = Label(text="km")
label3.grid(row=1,column=2)
label4 = Label(text="0")
label4.grid(row=1,column=1)
def calc():
    m = input.get()
    km = float(m) * 1.609
    label4.config(text=str(int(km)))
button = Button(text="Calculate",command =calc)
button.grid(row=2,column=1)























window.mainloop()