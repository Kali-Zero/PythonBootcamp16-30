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
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_button_clicked():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    label_checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button_clicked():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=RED, bg=YELLOW)
        print("Long Break Timer")
    elif reps % 2 == 0 :
        countdown(SHORT_BREAK_MIN * 60)
        label_timer.config(text="Break", fg=PINK, bg=YELLOW)
        print("Short Break Timer")
    else:
        countdown(WORK_MIN * 60)
        label_timer.config(text="Work", fg=GREEN, bg=YELLOW)
        print("Work Timer")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global reps
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0:
        count_seconds = "00" #Weird we can make it a string from an int,
    elif count_seconds < 10: #and then back to an int again (Dynamic Typing)
        count_seconds = "0" + str(count_seconds)
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_button_clicked()
        checkmarks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            checkmarks += "✔"
            label_checkmarks.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #
#https://colorhunt.co/
window = Tk()
window.title(" " * 45 + "Pomodoro") #Hacky way to center it. :-P
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

#fg = foreground color
label_timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

label_checkmarks = Label(font=(FONT_NAME, 12, "bold"), fg=GREEN, bg=YELLOW)
label_checkmarks.grid(column=1, row=3)

button_start = Button(window, text="Start", command=start_button_clicked, highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(window, text="Reset", command=reset_button_clicked, highlightthickness=0)
button_reset.grid(column=2, row=2)


window.mainloop()
