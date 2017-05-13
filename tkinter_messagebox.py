import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

def w_window():
    window.title('my window')
    window.geometry('300x200')  # width x height

def w_button():
    b = tk.Button(window, text='hit me', command=hit_me)
    b.pack()

def hit_me():
    #tk.messagebox.showinfo(title=':-)', message='you are so handsome')
    #tk.messagebox.showwarning(title=':-)', message='you are so handsome')
    #tk.messagebox.showerror(title=':-)', message='you are error')
    # ask = tk.messagebox.askquestion(title=':-)', message='you are handsome')#return 'Yes' or 'No'
    # if ask == 'yes':
    #     tk.messagebox.showwarning(title=':-)', message='you are so handsome')
    # else:
    #     tk.messagebox.showwarning(title=':-)', message='you are just so so')
    #tk.messagebox.askyesno(title=':-)', message='you are handsome')  # return False or True
    #tk.messagebox.askyesnocancel(title=':-)', message='you are handsome')  # return False or True
    tk.messagebox.askokcancel(title=':-)', message='you are handsome')  # return False or True

if __name__ == '__main__':
    w_window()
    w_button()
    window.mainloop()