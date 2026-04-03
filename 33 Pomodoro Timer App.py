import tkinter as tk
import  math

# Global Variables
reps = 0
timer = None

# Timer Reset
def reset_timer():
    global reps, timer
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg="green")
    check_marks.config(text="")
    reps = 0

# Get User Input
def get_times():
    try:
        work_min = int(work_input.get())
        short_min = int(short_input.get())
        long_min = int(long_input.get())
        return work_min * 60, short_min * 60, long_min * 60
    except:
        title_label.config(text="Invalid Input!", fg="red")
        return None, None, None

# Timer Start
def start_timer():
    global reps
    work_sec, short_sec, long_sec = get_times()

    if work_sec is None:
        return

    reps += 1

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg="red")
        count_down(long_sec)
    elif reps % 2 == 0:
        title_label.config(text="Short Break", fg="blue")
        count_down(short_sec)
    else:
        title_label.config(text="Work", fg="green")
        count_down(work_sec)

# Countdown
def count_down(count):
    global timer

    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        marks = ""
        work_Sessions = reps // 2
        for _ in range(work_Sessions):
            marks += "✔"

        check_marks.config(text=marks)

# UI setup
window = tk.Tk()
window.title("Custom Pomodoro Timer")
window.config(padx=50, pady=30, bg="#f7f5dd")

# Title
title_label = tk.Label(text="Timer", fg="green", bg="#f7f5dd", font=("Arial", 28, "bold"))
title_label.grid(column=1, row=0)

# Canvas
canvas = tk.Canvas(width=200, height=200, bg="#f7f5dd", highlightthickness=0)
canvas.create_rectangle(10, 10, 190, 190, outline="black", width=2)
timer_text = canvas.create_text(100, 100, text="00:00", fill="black", font=("Arial", 28, "bold"))
canvas.grid(column=1, row=1)

#-------- Input Fields -------
#Work Line
tk.Label(text="Work (min):", bg="#f7f5dd").grid(column=0, row=2)
work_input = tk.Entry(width=5)
work_input.insert(0, "25")
work_input.grid(column=0, row=3)

# Short Break
tk.Label(text="Short Break:", bg="#f7f5dd").grid(column=1, row=2)
short_input = tk.Entry(width=5)
short_input.insert(0, "5")
short_input.grid(column=1, row=3)

# Long Break
tk.Label(text="Long Break:", bg="#f7f5dd").grid(column=2, row=2)
long_input = tk.Entry(width=5)
long_input.insert(0, "15")
long_input.grid(column=2, row=3)

# Buttons
start_button = tk.Button(text="Start", width=10, command=start_timer)
start_button.grid(column=0, row=4)

reset_button = tk.Button(text="Reset", width=10, command=reset_timer)
reset_button.grid(column=2, row=4)

# Checkmarks
check_marks = tk.Label(fg="green", bg="#f7f5dd", font=("Arial", 14))
check_marks.grid(column=1, row=5)

# Run App
window.mainloop()
