from tkinter import *


def button_clicked():
    print("I got clicked!")
    new_text = entry.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)


#Label
my_label = Label(text="This is a label", font=('Arial', 24, 'bold'))
my_label.config(text='New Text')
my_label.grid(column=0, row=0)


#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="New Button")
button2.grid(column=2, row=0)


#Entry
entry = Entry(width=10)
print(entry.get())
entry.grid(column=3, row=2)

window.mainloop()
