import tkinter as tk

window = tk.Tk()

def w_window():
    window.title('my window')
    window.geometry('300x200') #width x height

def w_label():
    global var1
    var1 = tk.StringVar()
    l = tk.Label(window, textvariable=var1, bg='yellow',  width=8)
    l.pack()

def w_listbox():
    global var2, lb
    var2 = tk.StringVar()
    var2.set(('zero', 'second', 'third', 'fourth'))
    lb = tk.Listbox(window, listvariable=var2)
    list_item = (1, 2, 3, 4)
    for item in list_item:
        lb.insert('end', item)
    lb.insert(1, 'first')
    lb.insert('end', '13900124')
    lb.pack()

def w_button():
    b = tk.Button(window, text='print selection', command=print_selection)
    b.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

if __name__ == '__main__':
    w_window()
    w_label()
    w_button()
    w_listbox()
    window.mainloop()