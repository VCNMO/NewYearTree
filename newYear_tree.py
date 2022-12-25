import tkinter as tk

def left_mouse(event):
    if event.y > -2*event.x + 713:
        canvas.create_image(event.x, event.y, image=img_toy1)
        print(event.x, event.y)
    
def right_mouse(event):
    canvas.create_image(event.x, event.y, image=img_toy2)

win = tk.Tk()
canvas = tk.Canvas(win, width=800, height=700, bg='blue')
canvas.pack()

img_tree = tk.PhotoImage(file='fir_tree_800.png')
canvas.create_image(0,0, image=img_tree, anchor=tk.NW)

img_toy1 = tk.PhotoImage(file='ball3_small.png')
img_toy2 = tk.PhotoImage(file='ball5_small.png')

win.bind('<Button-1>', left_mouse)
win.bind('<Button-3>', right_mouse)

win.mainloop()

