
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW)

timer_text = Label(text="Timer", font=(FONT_NAME, 34, "normal"), bg=YELLOW, fg=GREEN)
timer_text.grid(column=1, row=0)

canvas = Canvas(width=200,height=234, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

import math
reps = 0
my_timer = None
def count_down(count=300):
    min = math.floor(count / 60)
    sec = count % 60
    if min < 10:
        min_txt = "0" + str(min)
    else:
        min_txt = str(min)
    if sec < 10:
        sec_txt = "0" + str(sec)
    else:
        sec_txt = str(sec)
    canvas.itemconfig(timer, text=f"{min_txt}:{sec_txt}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        finish.config(text=mark)


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_text.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_text.config(text="Work", fg=GREEN)

def reset_clicked():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer, text="00:00")
    timer_text.config(text="Timer")
    finish.config(text="")
    global reps
    reps = 0


start = Button(text= "Start", command = start_timer, highlightthickness=0)
reset = Button(text= "Reset", command = reset_clicked, highlightthickness=0)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)

finish = Label(text= "", font=(FONT_NAME, 14, "bold"), fg= GREEN, bg= YELLOW)
finish.grid(column=1, row=3)

window.mainloop()
