import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
counter = 0

def w_window():
    window.title('my window')
    window.geometry('300x200') #width x height

def w_label():
    global l
    l = tk.Label(window, bg='yellow',  width=25)
    l.pack()

def w_menubar():
    global menubar
    menubar = tk.Menu(window)
    filemenu = tk.Menu(menubar, tearoff=0)
    editmenu = tk.Menu(menubar, tearoff=0)
    addmenu = tk.Menu(filemenu, tearoff=0)
    menubar.add_cascade(label='File', menu=filemenu)
    menubar.add_cascade(label='Edit', menu=editmenu)

    filemenu.add_command(label='New', command=do_job)
    filemenu.add_command(label='Open', command=openfile)
    filemenu.add_command(label='Setting', command=do_job)
    filemenu.add_command(label='Save', command=do_job)

    filemenu.add_cascade(label='Add', menu=addmenu)
    addmenu.add_command(label='recent file', command=do_job)
    addmenu.add_command(label='project', command=do_job)

    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=window.quit)

    editmenu.add_command(label='copy', command=do_job)
    editmenu.add_command(label='cut', command=do_job)
    editmenu.add_command(label='paste', command=do_job)

def do_job():
    global counter
    l.config(text='doing the job '+str(counter))
    counter += 1

def openfile():
    r = filedialog.askopenfilename(title='打开文件', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*')])
    print(r)

if __name__ == '__main__':
    w_window()
    w_label()
    w_menubar()
    window.config(menu=menubar)
    window.mainloop()