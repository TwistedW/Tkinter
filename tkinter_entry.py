import tkinter as tk

window = tk.Tk()

def w_window():
    window.title('my window')
    window.geometry('300x200') #width x height

def w_entry():
    global e
    e = tk.Entry(window, show=None)
    e.pack()

def w_text():
    global t
    t = tk.Text(window, height=3, width=40)
    t.pack()

def w_button():
    b1 = tk.Button(window, text='insert point', command=insert_point)
    b1.pack()
    b2 = tk.Button(window, text='insert end', command=insert_end)
    b2.pack()

def insert_point():
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    t.insert('end', var)

if __name__ == '__main__':
    w_window()
    w_entry()
    w_button()
    w_text()
    window.mainloop()