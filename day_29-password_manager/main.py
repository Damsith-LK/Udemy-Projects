from tkinter import *
from tkinter import messagebox as msg

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email_ = email_entry.get()
    password = password_entry.get()

    # Checking if any field is empty
    if (' ' in website or len(website) == 0) or (' ' in email_ or len(email_) == 0) or (' ' in password or len(password) == 0):
        msg.showerror(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = msg.askyesno(title=website, message=f"These are the entered details\nEmail: {email}\nPassword: {password}\nDo you wish to proceed?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email_} | {password}\n")

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

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2, padx=5, pady=5)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

window.mainloop()