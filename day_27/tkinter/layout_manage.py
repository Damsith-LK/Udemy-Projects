# The main ways of managing layouts is pack(), place(), grid()
# We know pack() from before
# place() does precise positioning

import tkinter as tk

window = tk.Tk()
window.title("Managing Layouts")
window.maxsize(height=500, width=500)
window.minsize(height=500, width=500)
window.config(padx=20, pady=20)  # Adding a padding to the window and objects in it


def spin_box():
    print(spin.get())

# Place()
# We are getting this label to the center of the window
label = tk.Label(text="Using place()", font=("Ariel", 20, "italic"))
label.place(x=250, y=250, anchor="center")

# Grid()
# We can divide our window to any number of  vertical columns and horizontal rows with this
# But we can't have both pack() and grid() in the same code
# grid() is relative
spin = tk.Spinbox(from_=10, to=25, width=5, command=spin_box)
spin.grid(column=0, row=0)


window.mainloop()