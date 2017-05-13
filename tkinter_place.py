import tkinter as tk

window = tk.Tk()

def w_window():
    window.title('my window')
    window.geometry('300x200') #width x height

def w_canvas():
    global image, image_file
    canvas = tk.Canvas(window, height=150, width=500)
    canvas.grid(row=1, column=1)
    image_file = tk.PhotoImage(file='image.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)

def w_label():
    tk.Label(window, text='you are so handsome').pack(side='top')
    tk.Label(window, text='you are so handsome').pack(side='bottom')
    tk.Label(window, text='you are so handsome').pack(side='left')
    tk.Label(window, text='you are so handsome').pack(side='right')

def w_label_change():
    for i in range(4):
        for j in range(3):
            tk.Label(window, text='you are so handsome').grid(row=i, column=j, padx=10, pady=10)

def w_label_place():
    tk.Label(window, text='you are so handsome').place(x=150, y=100, anchor='center')

if __name__ == '__main__':
    w_window()
    w_label_change()
    window.mainloop()