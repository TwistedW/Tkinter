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

def w_text():
    global t
    t = tk.Text(window, height=2, width=15, bg='green')
    t.pack()

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var = 'you hit me'
        t.insert('insert', var)
    else:
        t.delete(0.0, 'end')
        on_hit = False
        t.insert('insert', ' ')

def w_button():
    b = tk.Button(window, text='my tk button', bg='red', font=('Arial', 12),
                  width=15, height=2, command=hit_me)
    b.pack()

if __name__ == '__main__':
    w_window()
    w_text()
    w_label()
    w_button()
    window.mainloop()
