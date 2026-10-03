from tkinter import *

#Creating a new window and changing its configurations
window = Tk()
window.title("My first GUI program")   #changing the title of the window
window.minsize(width=500, height=500)  #setting the minimum dimensions for the window

#Widget 1: Labels
label = Label(text="This is the old text")
label.config(text="This is the new text")  #Updating the label's text value
label.pack()     #Makes sure to print the label on the screen

#Widget 2: Buttons
def button_clicked():
    print("Do something")
    print(entry.get())
    print(text.get("1.0", END))


button = Button(text="Click Me!", command=button_clicked)  #Setting a text display on the button and getting it to do something
button.pack()

#Widget 3: Entries
entry = Entry(width=40) #Setting the width of the entry box
#adding some text to begin with
entry.insert(END, string="Start typing...")
#get the text from the entry box
print(entry.get())
entry.pack()

#Widget 4: Text
text = Text(height=5, width=30) # You can set the number of lines as the height
text.focus() #Puts a cursor in the textbox
text.insert(END, "Example of a multi-line entry") #Adds some text to begin with
print(text.get("1.0", END)) #Gets the current value at line 1, character 0
text.pack()

#Widget 5: Spinbox
#getting the spinbox to be tied to a function to get hold of its value
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=20, width=5, command=spinbox_used)
spinbox.pack()

#Widget 6: Scale
#Call the current scale value
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=10, command=scale_used)
scale.pack()

#Widget 7: Checkbox
def checkbox_used():
    #Prints 1 if button was checked, else prints 0
    print(checked_state.get())


checked_state = IntVar() #creating a variable to keep track of the value of the checkbox
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbox_used)
checked_state.get()
checkbutton.pack()


#Widget 8: Radiobutton
def radio_used():
    print(radio_state.get())

#Variable to hold on to which radiobutton is checked
radio_state = IntVar()
#both the buttons are created like 2 objects from the Radiobutton class
radio_button1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radio_button2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()

#Widget 9: Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ['apple', 'banana', 'orange', 'pear']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()