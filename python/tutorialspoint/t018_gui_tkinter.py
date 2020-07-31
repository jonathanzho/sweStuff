import tkinter as tk

def handle_button1_click(event):
    print('button1 was clicked!')

def main():
    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack()

    button1 = tk.Button(frame,
        text='Click me!',
        width=20,
        height=10,
        bg='white',
        fg='red')
    button1.pack()
    button1.bind('<Button-1>', handle_button1_click)

    root.mainloop()

if __name__ == '__main__':
    main()
