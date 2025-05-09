import math
from tkinter import *

# -------------------------------
# Some improvements to be made:
#     Bring the window to the front when it's time for a break
#     Play sound when break is over


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
MIN_TO_SEC = 60
reps = 0
timer_count_down = None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    canvas.itemconfig(txt_time_elapsed, text="00:00")
    lbl_title.config(text="Timer", fg=GREEN)
    lbl_check_mark.config(text="")

    global reps, timer_count_down
    reps = 0
    window.after_cancel(timer_count_down)



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_pomodoro():
    work_sec = WORK_MIN * MIN_TO_SEC
    short_break_sec = SHORT_BREAK_MIN * MIN_TO_SEC
    long_break_sec = LONG_BREAK_MIN * MIN_TO_SEC

    global reps
    reps += 1

    if reps % 8 == 0: # 8th rep
        lbl_title.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    if reps % 2 > 0: # If it's the 1st, 3rd, 5th or 7th rep -- work time
        lbl_title.config(text="Work", fg=GREEN)
        count_down(work_sec)
    else: # if it's the 2nd, 4th, 6th  -- take a short break
        lbl_title.config(text="Break", fg=PINK)
        count_down(short_break_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    # "00:00"
    # get_minutes = round down(count / 60)
    # get_seconds = count % 60
    count_min = math.floor(count / MIN_TO_SEC)
    count_seconds = count % MIN_TO_SEC

    # Can also format numbers via dynamic typing: example -
    #   if count_seconds < 10: #count_seconds is an int
    #       count_seconds = f"0{count_seconds}" #count_seconds is now a string

    global timer_count_down

    canvas.itemconfig(txt_time_elapsed, text=f"{count_min:02}:{count_seconds:02}")
    if count > 0:
        timer_count_down = window.after(1000, count_down, count-1)
    else:
        start_pomodoro()
        if reps % 2 == 0:
            check_marks = CHECK_MARK * int(reps / 2)
            lbl_check_mark.config(text=check_marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.minsize(width=300, height= 300)
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro timer")



bg_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
    # - create canvas with slightly bigger width and height than the background image
    #       same background color as the window and
    #       set the highlight thickness = 0 in order to remove the image borders
canvas.create_image(105, 112, image=bg_image)
txt_time_elapsed = canvas.create_text(105,130,text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

lbl_title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
lbl_title.grid(column=1, row=0)

btn_start = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 10, "bold"), command=start_pomodoro)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 10, "bold"), command=reset_timer)
btn_reset.grid(column=2, row=2)

lbl_check_mark = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
lbl_check_mark.grid(column=1, row=3)

window.mainloop()