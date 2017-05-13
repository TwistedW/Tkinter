import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()

def w_window():
    window.title('my window')
    window.geometry('400x200') #width x height

def w_frame():
    global frm
    frm = tk.Frame(window)
    frm.pack()

def w_frame_label():
    tk.Label(frm, width=8, height=3).pack()

def w_simpledialog():
    btn1 = tk.Button(frm, text='Input String', command=inputStr)
    btn2 = tk.Button(frm, text='Input Integer', command=inputInt)
    btn3 = tk.Button(frm, text='Input Float', command=inputFloat)

    btn1.pack(side='left')
    btn2.pack(side='left')
    btn3.pack(side='left')

def inputStr():
    r = simpledialog.askstring('Python Tkinter', 'Input String', initialvalue='Python Tkinter')
    print(r)
def inputInt():
    r = simpledialog.askinteger('Python Tkinter', 'Input Integer')
    print(r)
def inputFloat():
    r = simpledialog.askfloat('Python Tkinter', 'Input Float')
    print(r)

if __name__ == '__main__':
    w_window()
    w_frame()
    w_frame_label()
    w_simpledialog()
    window.mainloop()