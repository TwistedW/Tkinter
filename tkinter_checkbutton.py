import tkinter as tk

window = tk.Tk()

def w_window():
    window.title('my window')
    window.geometry('300x200') #width x height

def w_label():
    global l
    l = tk.Label(window, bg='yellow',  width=25)
    l.pack()

def w_checkbutton():
    global var1, var2
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=check_selection)
    c1.pack()
    c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=check_selection)
    c2.pack()

def check_selection():
    if(var1.get() == 1)&(var2.get() == 0):
        l.config(text='I only love Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I only love C++ ')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either ')
    else: 
        l.config(text='I love both ')

if __name__ == '__main__':
    w_window()
    w_label()
    w_checkbutton()
    window.mainloop()