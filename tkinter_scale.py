import tkinter as tk

window = tk.Tk()

def w_window():
    window.title('my window')
    window.geometry('300x200') #width x height

def w_label():
    global l
    l = tk.Label(window, bg='yellow',  width=25)
    l.pack()

def w_scale():
    s = tk.Scale(window, label='drag', from_=0, to=12, orient=tk.HORIZONTAL, length=300,
                 showvalue=0, tickinterval=3, resolution=0.001, command=drag_selection)
    s.pack()

def drag_selection(v):
    l.config(text='you have dragged to '+v)

if __name__ == '__main__':
    w_window()
    w_label()
    w_scale()
    window.mainloop()