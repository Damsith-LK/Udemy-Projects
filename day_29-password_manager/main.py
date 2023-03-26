from tkinter import *
from tkinter import messagebox as msg
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)  # With this, when a password is generated we copy it to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email_ = email_entry.get()
    password = password_entry.get()

    data_dict = {
        website: {
            "email": email_,
            "password": password
        }
    }

    # Checking if any field is empty
    if (' ' in website or len(website) == 0) or (' ' in email_ or len(email_) == 0) or (' ' in password or len(password) == 0):
        msg.showerror(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = msg.askyesno(title=website, message=f"These are the entered details\nEmail: {email_}\nPassword: {password}\nDo you wish to proceed?")

        if is_ok:
            with open("data.json", "w") as file:
                json.dump(data_dict, file)

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=20)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="w")
with open('email.txt', 'r') as file:
    email = file.read()
email_entry.insert(0, email)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

generate_password_button = Button(text="Generate Password", command=gen_password)
generate_password_button.grid(row=3, column=2, padx=5, pady=5)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

window.mainloop()