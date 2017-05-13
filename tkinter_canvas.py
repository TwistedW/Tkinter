import tkinter as tk

window = tk.Tk()

def w_window():
    window.title('my window')
    window.geometry('300x200') #width x height

def w_button():
    b = tk.Button(window, text='move', bg='green', command=moveit)
    b.pack()

def w_canvas():
    global canvas, image_file, image, line, oval, arc, rect
    canvas = tk.Canvas(window, bg='blue', height=100, width=300)
    image_file = tk.PhotoImage(file='image.gif')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    x0, y0, x1, y1 = 50, 50, 80, 80
    line = canvas.create_line(x0, y0, x1, y1)
    oval = canvas.create_oval(x0-30, y0-30, x1-30, y1-30, fill='red')
    arc = canvas.create_arc(x0 + 30, y0 + 30, x1 + 30, y1 + 30, start=0, extent=160, fill='yellow')
    rect = canvas.create_rectangle(100, 30, 100 + 20, 30 + 20)
    canvas.pack()

def moveit():
    canvas.move(oval, 10, 2)

if __name__ == '__main__':
    w_window()
    w_canvas()
    w_button()
    window.mainloop()