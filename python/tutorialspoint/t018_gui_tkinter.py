import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
    
        frame = tk.Frame(parent)
        frame.pack()

        button1 = tk.Button(frame,
            text='Click me!',
            fg='red',
            highlightbackground='green')
        button1.pack()
        button1.bind('<Button-1>', self.handle_button1_click)

    def handle_button1_click(self, event):
        print('button1 was clicked!')

def main():
    root = tk.Tk()
    root.geometry('400x200')

    app = MainApplication(root)
    app.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
