from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def write_to_file():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    web_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showerror(title="Error", message="Please don't leave any fields empty.")
        
    else:
        is_ok =  messagebox.askokcancel(title= website,message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json","r") as f:
                    d = json.load(f)
                    d.update(web_data)
            except FileNotFoundError:
                with open("data.json","w") as f:
                    json.dump(web_data,f,indent=4)
            else:
                with open("data.json","w") as f:
                    json.dump(d,f,indent=4)
            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_list = [random.choice(letters) for item in range(nr_letters)]
    password_list += [random.choice(symbols) for item in range(nr_symbols)]
    password_list += [random.choice(numbers) for item in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)  # Copy the generated password to clipboard

def find_password():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        entered = web_entry.get()
        if entered in data:
            email = data[entered]["email"]
            password = data[entered]["password"]
            messagebox.showinfo(title=entered, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists.")
    web_entry.delete(0, END) 

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")
canvas = Canvas(height=200,width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0,column=1)

web_label = Label(text="Website:")
web_label.grid(row=1,column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1,column=1)
web_entry.focus()

search_button = Button(text="Search",command=find_password)
search_button.grid(row=1,column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"shubiks@gmail.com")

pass_label = Label(text="Password:")
pass_label.grid(row=3,column=0)

pass_entry = Entry(width=21)
pass_entry.grid(row=3,column=1)


gen_button = Button(text="Generate Password",command=generate_password)
gen_button.grid(row=3,column=2)

add_button = Button(text="Add",width=34,command=write_to_file)
add_button.grid(row=4,column=1,columnspan=2)




window.mainloop()