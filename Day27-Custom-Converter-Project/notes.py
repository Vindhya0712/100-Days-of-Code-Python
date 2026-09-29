# import tkinter
#
# window = tkinter.Tk()
# window.title("My first GUI Program")
# window.minsize(width=500, height=300)
#
# # label
# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack(expand=True)
#
# window.mainloop()

def add(*args):
    summ = 0
    for n in args:
        summ += n
    return summ


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)
