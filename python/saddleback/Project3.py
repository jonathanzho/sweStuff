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

        gridFrame = tk.Frame(parent)

        labelName = tk.Label(gridFrame,
                             text='Name',
                             justify='center')
        labelName.grid(row=0, column=0)

        entryName = tk.Entry(gridFrame,
                             bd=5)
        entryName.grid(row=0, column=1)

        labelIdNumber = tk.Label(gridFrame,
                             text='ID Number',
                             justify='center')
        labelIdNumber.grid(row=1, column=0)

        entryIdNumber = tk.Entry(gridFrame,
                             bd=5)
        entryIdNumber.grid(row=1, column=1)

        labelDepartment = tk.Label(gridFrame,
                             text='Department',
                             justify='center')
        labelDepartment.grid(row=2, column=0)

        entryDepartment = tk.Entry(gridFrame,
                             bd=5)
        entryDepartment.grid(row=2, column=1)

        labelJobTitle = tk.Label(gridFrame,
                             text='Job Title',
                             justify='center')
        labelJobTitle.grid(row=3, column=0)

        entryJobTitle = tk.Entry(gridFrame,
                             bd=5)
        entryJobTitle.grid(row=3, column=1)

        buttonAddToFile = tk.Button(gridFrame,
                                    borderwidth=5,
                                    fg='red',
                                    text='Add to File')
        buttonAddToFile.grid(row=4, column=1)

        gridFrame.pack(side='top')

def main():
    root = tk.Tk()
    root.geometry('400x200')
    root.title('Employee')
    
    app = MainApplication(root)
    app.pack(side="top", fill="both", expand=True)
    
    root.mainloop()

if __name__ == '__main__':
    main()
