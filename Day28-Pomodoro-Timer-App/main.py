from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    """A function tied to the press of the start button to start a countdown"""

    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        timer.config(text="Work", fg=GREEN)
        countdown(work_sec)
    #how do i get it to countdown from say 5 minutes? Well, gotta multiply 5 by 60, so that when the
    # countdown function gets called, it counts down for 300 seconds....which is essentially 5 mins....but there's a bit
    #of a design issue....cuz the timer shows an explicit countdown from 300...we don't want that...what to do?


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    """A recursive function that changes the timer_text on every run"""

    #total seconds / 60 = minutes remaining
    count_min = math.floor(count / 60)
    #total seconds % 60 = seconds remaining
    count_sec = count % 60

    #Dynamic Typing makes my life easy here!
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min == 0:
        count_min = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count-1)
    else:
        start_timer() #calling the timer function again once we count down to zero
        #for every 2 reps, we have completed one 25min work session...one checkmark for every work session
        marks = ""
        for i in range(0, math.floor(reps/2)):
            marks += "✅"
        tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Vindhya's Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold')) #created it as a variable so that i can change its value in tied functions
canvas.grid(row=1, column=1)

timer = Label(text="Timer", font=(FONT_NAME, 45, 'bold'), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer) #tied the function call to the button press
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=2)

tick = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0) #start out as empty
tick.grid(row=3, column=1)

window.mainloop()
