import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

def w_window():
    window.title('my window')
    window.geometry('300x200') #width x height

def openfile():
    r = filedialog.askopenfilename(title='打开文件', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*')])
    print(r)

def savefile():
    r = filedialog.asksaveasfilename(title='保存文件', initialfile='hello.text')
    print(r)

def w_frame():
    global frm
    frm = tk.Frame(window)
    frm.pack()

def w_frame_label():
    tk.Label(frm, width=8, height=3).pack()

def w_filedialog():
    btn1 = tk.Button(frm, text='File Open', command=openfile)
    btn2 = tk.Button(frm, text='File Save', command=savefile)
    btn1.pack(side='left')
    btn2.pack(side='right')

if __name__ == '__main__':
    w_window()
    w_frame()
    w_frame_label()
    w_filedialog()
    window.mainloop()