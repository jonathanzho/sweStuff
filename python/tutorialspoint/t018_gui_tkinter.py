import tkinter as tk

def handle_button1_click(event):
    print('button1 was clicked!')

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
    
        frame = tk.Frame(parent)
        frame.pack()

        button1 = tk.Button(frame,
            text='Click me!',
            width=20,
            height=10,
            bg='white',
            fg='red')
        button1.pack()
        button1.bind('<Button-1>', handle_button1_click)

def main():
    root = tk.Tk()

    app = MainApplication(root)
    app.pack(side='top', fill='both', expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()
