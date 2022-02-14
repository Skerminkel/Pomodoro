from tkinter import *
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
main_count = None

# ---------------------------- TIMER RESET ------------------------------- # 


def timer_reset():
    global reps
    reps = 1

    start.config(state="normal")
    reset.config(state="disabled")

    win.after_cancel(main_count)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_label.config(text="TIMER", bg=YELLOW, font=(FONT_NAME, 40, "bold"), fg=GREEN)
    phase_check.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def timer_start():

    global reps

    reset.config(state="normal")
    start.config(state="disabled")

    if reps % 2 != 0 and reps <= 7:
        messagebox.showinfo(title="Work", message="Start working~")
        countdown_timer(WORK_MIN*60)
        timer_label.config(text=f"Work")
        phase_check.config(text=f'{"✔"*(reps//2)}')
        print(reps)

    elif reps % 2 == 0 and reps <= 7:
        messagebox.showinfo(title="Work", message="Small break!")
        countdown_timer(SHORT_BREAK_MIN*60)
        timer_label.config(text=f"Short Break", fg=PINK)

    elif reps == 8:
        messagebox.showinfo(title="Break", message="Long break!")
        countdown_timer(LONG_BREAK_MIN*60)
        timer_label.config(text=f"Long Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown_timer(time):
    global reps, main_count
    count_min = time//60
    count_sec = time % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")

    if time > 0:

        main_count = win.after(1000, countdown_timer, time - 1)

    elif time == 0:
        reps += 1
        timer_start()

# ---------------------------- UI SETUP ------------------------------- #


win = Tk()
win.title("Pomodoro")
win.config(padx=100, pady=50, bg=YELLOW)
TOMATO = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=280, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 146, image=TOMATO)
timer_text = canvas.create_text(100, 166, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="TIMER", bg=YELLOW, font=(FONT_NAME, 40, "bold"), fg=GREEN)
timer_label.grid(column=1, row=0, sticky="s")

start = Button(padx=5, pady=5, text="Start", command=timer_start, bg=YELLOW, highlightthickness=0, bd=0,
               font=(FONT_NAME, 12, "underline"))
start.grid(column=0, row=2)

reset = Button(padx=5, pady=5, text="Reset", command=timer_reset, bg=YELLOW, highlightthickness=0, bd=0,
               font=(FONT_NAME, 12, "underline"))
reset.grid(column=2, row=2)

phase_check = Label(text="", padx=5, pady=5, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
phase_check.grid(column=1, row=3)

win.mainloop()