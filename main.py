from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = 'white'
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
check_mark_text = ''


def reset_timer():
    window.after_cancel(timer)
    global check_mark_text
    global reps
    timer_label.config(text='TIMER', fg=GREEN)
    canvas.itemconfig(timer_text, text='00:00')
    check_mark_text = ''
    check_mark.config(text="")
    reps = 0


def start_timer():
    global check_mark_text
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # 1,2,3,4,5,6,7,8
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Break', fg=PINK)
        check_mark_text += '✔'
        check_mark.config(text=check_mark_text)

    else:
        count_down(work_sec)
        timer_label.config(text='Work', fg=GREEN)


def count_down(sec):
    global timer
    count_min = sec // 60
    count_sec = sec % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if sec > 0:
        timer = window.after(10, count_down, sec - 1)
    else:
        start_timer()


window = Tk()
window.title('Pomodoro Timer')
window.config(padx='10', pady='5', bg=YELLOW)

timer_label = Label(text='Timer', font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 10), bg=PINK,
                      fg=WHITE, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

check_mark = Label(text=check_mark_text, font=(FONT_NAME, 15, 'bold'), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 10), bg=PINK,
                      fg=WHITE, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# window.attributes('-topmost', True)

window.mainloop()
