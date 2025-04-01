from tkinter import *

window = Tk()
window.minsize(width=500, height = 300)
window.title("Miles to KM Converter")

miles_input = Entry(width=20)
miles_input.grid(column=1, row=0)
print(miles_input.get())

miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

text = Label(text="is equal to", font=("Arial", 24, "bold"))
text.grid(column=0, row=1)
text.config(padx=10, pady=10)

km_value = Label(text="0", font=("Arial", 24, "bold"))
km_value.grid(column=1, row=1)
km_value.config(padx=10, pady=10)

km_label = Label(text="km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

def func():
    miles_val = int(miles_input.get())
    result = round(miles_val * 1.6, 2)
    km_value.config(text=result)

button = Button(text="Calculate", command=func)
button.grid(column=1, row=2)

window.mainloop()