from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    dict_words = original_data.to_dict(orient="records")
else:
    dict_words = data.to_dict(orient="records")

random_row = {}
def get_word():
    global random_row,flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous flip timer
    random_row = random.choice(dict_words)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=random_row["French"],fill="black")
    canvas.itemconfig(card_bg,image=front_img)
    window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word,text=random_row["English"],fill="white")
    canvas.itemconfig(card_bg,image=back_img)

def is_known():
    dict_words.remove(random_row)
    c = pandas.DataFrame(dict_words)
    c.to_csv("./data/words_to_learn.csv",index=False)
    get_word()
     

window = Tk()
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(400,280,image=front_img)
title = canvas.create_text(400,150,text="French",font=("Arial",40,"italic"),fill="black")
word = canvas.create_text(400,263,text="Historie",font=("Arial",60,"bold"),fill="black")
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)




cross_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_img)
wrong_button.config(bg=BACKGROUND_COLOR,highlightthickness=0,command=get_word)
wrong_button.grid(row=1,column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img)
right_button.config(bg=BACKGROUND_COLOR,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

get_word()
window.mainloop()
