import tkinter as tk

on_hit = False
window = tk.Tk()
var = tk.StringVar()

def w_window():
    window.title('my window')
    window.geometry('400x400') #width x height

def w_label():
    global l, l2
    l = tk.Label(window, text='on my window', bg='yellow')
    l.pack()
    l2 = tk.Label(window, textvariable=var)
    l2.pack()

def w_frame_label():
    tk.Label(frm_left, text='on the frm_left1').pack()
    tk.Label(frm_left, text='on the frm_left2').pack()
    tk.Label(frm_right, text='on the frm_right').pack()

def w_frame():
    global frm, frm_left, frm_right
    frm = tk.Frame(window)
    frm.pack()
    frm_left = tk.Frame(frm)
    frm_left.pack(side='left')
    frm_right = tk.Frame(frm)
    frm_right.pack(side='right')

def w_button():
    b = tk.Button(frm_right, text='my TK Button', bg='green', command=hit_me)
    b.pack()

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

if __name__ == '__main__':
    w_window()
    w_label()
    w_frame()
    w_frame_label()
    w_button()
    window.mainloop()