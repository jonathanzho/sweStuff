import tkinter as tk

def handle_button1_click(event):
    print('button1 was clicked!')

window = tk.Tk()

frame = tk.Frame(window)
frame.pack()

button1 = tk.Button(frame,
    text='Click me!',
    width=20,
    height=10,
    bg='white',
    fg='red'
    )
button1.pack()
button1.bind('<Button-1>', handle_button1_click)

window.mainloop()
