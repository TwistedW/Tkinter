import tkinter as tk

window = tk.Tk()

def w_window():
    window.title('my window')
    window.geometry('300x200') #width x height

def w_label():
    global var, l
    var = tk.StringVar()
    l = tk.Label(window, bg='yellow',  width=20, text='empty')
    l.pack()

def w_radiobutton():
    r1 = tk.Radiobutton(window, text='OptionA', variable=var, value='A', command=print_selection)
    r1.pack()
    r2 = tk.Radiobutton(window, text='OptionB', variable=var, value='B', command=print_selection)
    r2.pack()
    r3 = tk.Radiobutton(window, text='OptionC', variable=var, value='C', command=print_selection)
    r3.pack()
    r4 = tk.Radiobutton(window, text='OptionD', variable=var, value='D', command=print_selection)
    r4.pack()

def print_selection():
    l.config(text='you have selected'+var.get())

if __name__ == '__main__':
    w_window()
    w_label()
    w_radiobutton()
    window.mainloop()