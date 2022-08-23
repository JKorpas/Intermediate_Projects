from tkinter import *
import time


TIME_FONT = ('Arial', 24, 'bold')
TITLE_FONT = ('Arial', 44, 'bold')
CHECKMARK = "✔"
CHECKMARKS = ""
TIME_TO_LEARN = 1
SHORT_BREAK = 5
LONG_BREAK = 20
reps = 0
TIMER = None

# TIMER
def start_timer():
    global reps
    global CHECKMARKS
    global CHECKMARK
    reps += 1
    work_sec = 1
    short_break_sec = 1
    long_break_sec = 1

    if reps % 8 == 0:
        title_label.config(text="Break")
        count_down(long_break_sec)
        CHECKMARKS = ""
        check_mark.config(text=f"{CHECKMARKS}")
    elif reps % 2 == 0:
        title_label.config(text="Break")
        count_down(short_break_sec)
        CHECKMARKS += CHECKMARK
        check_mark.config(text=f"{CHECKMARKS}")
    else:
        title_label.config(text="Work")
        count_down(work_sec)


# COUNT DOWN
def count_down(count):
    global TIMER
    if count > 0:
        mins, secs = divmod(count, 60)
        TIMER = '{:02d}:{:02d}'.format(mins, secs)
        canvas.itemconfig(timer_text, text=f"{TIMER}")
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
# Chill Time


def chill(count):
    pass


# RESET

def reset_timer():
    window.after_cancel(TIMER)
    CHECKMARKS = ""
    check_mark.config(text=f"{CHECKMARKS}")
    title_label.config(text='Timer')
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

# UI


window = Tk()
window.title("Pomodoro Time Manager")
window.config(padx=100, pady=50)
# Timer text
title_label = Label(text="Timer", fg="black", font=TITLE_FONT, )
title_label.grid(column=1, row=0, padx=12)

# Photo
canvas = Canvas(width=200, height=224, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=TIME_FONT)
canvas.grid(column=1, row=1)
# Start/Resten Button
start_button = Button(window, text="Start", command=start_timer)
start_button.grid(column=0, row=2, padx=12)
reset_button = Button(window, text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2, padx=12)
# Checkmark

check_mark = Label(text=f"{CHECKMARKS}")
check_mark.grid(column=1, row=3, padx=12)
window.mainloop()
