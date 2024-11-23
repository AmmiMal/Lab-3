import tkinter as tk
from tkinter import messagebox
from keygeneration import key_generation
from pygame import mixer



def click():
    number = num_enter.get()
    if not number.isdigit():
        tk.messagebox.showwarning('Error', 'Введено не число')
        return 0
    else:
        if len(number) == 3 and number[0] != '0':
            your_key = key_generation(number)
            key = tk.Label(frame, font=('Georgia', 15), bg='#FFE4E1', fg='#B22222')
            key.grid(column=1, row=1, padx=10, pady=15)
            key.configure(text=your_key)
        else:
            tk.messagebox.showwarning('Error', 'Введено не трехзначное число')
        return 0


def animation():
    canvas = tk.Canvas(frame, bg='#FFE4E1', width=150, height=50, borderwidth=0, highlightthickness=0)
    canvas.grid(column=1, row=8, padx=30, pady=15)
    canvas_text = canvas.create_text(10, 10, text='', anchor=tk.NW, font=('Georgia', 25), fill='#B22222')
    text_string = "Wild Rift"

    delta = 500
    delay = 0

    for i in range(len(text_string) + 1):
        s = text_string[:i]
        update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
        canvas.after(delay, update_text)
        delay += delta


window = tk.Tk()
window.title('Генератор ключа')
window.geometry('700x400')
bg_img = tk.PhotoImage(file='lol.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg='#FFE4E1')
frame.place(relx=0.5, rely=0.5, anchor='center')

lbl_enter_num = tk.Label(frame, text='Введите трехзначное число',
                         font=('Georgia', 15), bg='#FFE4E1', fg='#B22222')
lbl_enter_num.grid(column=0, row=0, padx=10, pady=15)

num_enter = tk.Entry(frame, width=10, font=('Georgia', 15))
num_enter.grid(column=1, row=0, padx=30, pady=15)

btn = tk.Button(frame, text="OK", font=('Georgia', 15), bg='#B22222', fg='white', command=click)
btn.grid(column=2, row=0, padx=10, pady=15)

lbl_enter_num = tk.Label(frame, text='Ваш сгенерированный ключ:',
                         font=('Georgia', 15), bg='#FFE4E1', fg='#B22222')
lbl_enter_num.grid(column=0, row=1, padx=10, pady=15)
animation()

mixer.init()
mixer.music.load("music.wav")
mixer.music.set_volume(0.01)
mixer.music.play(77)

window.mainloop()





