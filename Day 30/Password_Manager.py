# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
import json
def random_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
import pandas
from tkinter import messagebox

def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure all fields are entered.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nUsername: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                email_input.delete(0, END)
                email_input.insert(0, "jeremy.life0107@gmail.com")
                password_input.delete(0, END)

def search():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            try:
                email = data[website]["email"]
                password = data[website]["password"]
            except:
                messagebox.showinfo(title="Oops", message=f"No website data for {website} found.")
            else:
                messagebox.showinfo(title= website,  message=f"Username/Email: {email}\nPassword: {password}")

    except:
        messagebox.showinfo(title="Oops", message="No data file found.")

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

website_input = Entry(width=27)
website_input.grid(column=1, row=1)
email_input = Entry(width=45)
email_input.insert(0, "jeremy.life0107@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=27)
password_input.grid(column=1, row=3)

search_btn = Button(text="Search", width=14, command=search)
search_btn.grid(column=2, row=1)
generate_btn = Button(text="Generate Password", width=14, command=random_password)
generate_btn.grid(column=2, row=3)
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
