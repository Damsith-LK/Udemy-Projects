import tkinter as tk

# Creating a window
window = tk.Tk()
window.title("Learning Tkinter")
window.minsize(width=500, height=500)
window.maxsize(width=500, height=500)

# Creating a label on the window
label = tk.Label(text="This is a label", font=("Times New Roman", 30, "bold"))
label.pack()

# Changing the label
label.config(text="Label Updated.")

# Buttons
button = tk.Button(text="Click this button")
button.pack()

# Entry (Getting inputs)
entry = tk.Entry()
entry.pack()


def button_clicked():
    inp = entry.get()
    label.config(text=inp)


button.config(command=button_clicked)


window.mainloop()
