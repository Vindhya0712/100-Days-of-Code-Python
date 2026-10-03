from tkinter import *


def button_clicked():
    miles_input = int(entry.get())
    km_output = round((miles_input * 1.60934), 2)
    answer.config(text=km_output)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=30, pady=30)

#Miles
miles = Label(text="Miles")
miles.grid(column=2, row=0)
#is equal to
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)
#Km
km = Label(text="Km")
km.grid(column=2, row=1)
#entry
entry = Entry(width=15)
entry.grid(column=1, row=0)
#answer
answer = Label(text='0')
answer.grid(column=1, row=1)
#Calculate button
calc = Button(text="Calculate", command=button_clicked)
calc.grid(column=1, row=2)


window.mainloop()
