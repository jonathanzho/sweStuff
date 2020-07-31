# =========
# Project 3
# =========

import tkinter as tk

class Employee:
    def __init__(self, name, idNumber, department, jobTitle):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.jobnTitle = jobTitle

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        button1 = tk.Button(parent, text='Click Me!')
        button1.pack(side="top", fill="both", expand=True)


def main():
    root = tk.Tk()
    app = MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

if __name__ == '__main__':
    main()
