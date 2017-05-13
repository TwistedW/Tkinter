import tkinter as tk

on_hit = False
window = tk.Tk()
var = tk.StringVar()

def w_window():
    window.title('my window')
    window.geometry('300x200')  # width x height

def w_label():
    l = tk.Label(window, textvariable=var, bg='white', font=('Arial', 12),
                 width=15, height=2)
    l.pack()

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

def w_button():
    b = tk.Button(window, text='my TK Button', bg='green', font=('Arial', 12),
                  width=15, height=2, command=hit_me)
    b.pack()

if __name__ == '__main__':
    w_window()
    w_label()
    w_button()
    window.mainloop()
