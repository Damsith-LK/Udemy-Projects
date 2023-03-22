import tkinter as tk

# creating the window
window = tk.Tk()
window.title("Miles to Kilo Meters Converter")
window.eval('tk::PlaceWindow . center')
window.minsize(height=200, width=400)
window.maxsize(height=200, width=400)
window.config(padx=10, pady=10)

# The labels here
miles_label = tk.Label(text="Miles", font=("Courier", 15, 'bold'))
miles_label.place(x=300, y=50, anchor="center")

equal_label = tk.Label(text="is equal to", font=("Courier", 15, 'bold'))
equal_label.place(x=60, y=100, anchor='center')

kilo_label = tk.Label(text=0, font=("Courier", 15, 'bold'))
kilo_label.place(x=200, y=100, anchor='center')

km_label = tk.Label(text='km', font=("Courier", 15, 'bold'))
km_label.place(x=300, y=100, anchor="center")


window.mainloop()