# =========
# Project 4 
# =========

import os
import sqlite3 as lite
import tkinter as tk

class Employee:
    def __init__(self, name, idNumber, department, jobTitle):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.jobTitle = jobTitle

    def insert_file(self):
        if not self.name:
            # Exit a GUI program:
            os._exit(0)
        file = open('Project3_Employees.txt', 'a')
        file.write('{},{},{},{}\n'.format(
            self.name,
            self.idNumber,
            self.department,
            self.jobTitle))
        file.close()

    def read_data_from_db():
        con = lite.connect('CIMP8A.db')
        cur = con.cursor()
    
        cur.execute("SELECT * FROM Employee")
        dbData = cur.fetchall()
        print(dbData)
    
        cur.close()
        con.close()

        return dbData

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # Current employee index:
        self.empIndex = 0

        # GUI widgets:
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        gridFrame = tk.Frame(parent)
        gridFrame.pack(side='top')

        labelName = tk.Label(gridFrame,
                             text='Name',
                             justify='center')
        labelName.grid(row=0, column=0)

        self.entryName = tk.Entry(gridFrame,
                             bd=5)
        self.entryName.grid(row=0, column=1)

        labelIdNumber = tk.Label(gridFrame,
                             text='ID Number',
                             justify='center')
        labelIdNumber.grid(row=1, column=0)

        self.entryIdNumber = tk.Entry(gridFrame,
                             bd=5)
        self.entryIdNumber.grid(row=1, column=1)

        labelDepartment = tk.Label(gridFrame,
                             text='Department',
                             justify='center')
        labelDepartment.grid(row=2, column=0)

        self.entryDepartment = tk.Entry(gridFrame,
                             bd=5)
        self.entryDepartment.grid(row=2, column=1)

        labelJobTitle = tk.Label(gridFrame,
                             text='Job Title',
                             justify='center')
        labelJobTitle.grid(row=3, column=0)

        self.entryJobTitle = tk.Entry(gridFrame,
                             bd=5)
        self.entryJobTitle.grid(row=3, column=1)

        buttonAddToFile = tk.Button(gridFrame,
                                    borderwidth=5,
                                    fg='red',
                                    text='Add to File')
        buttonAddToFile.grid(row=4, column=1)
        buttonAddToFile.bind('<Button-1>', self.buttonAddToFile_cb)

        buttonNewData = tk.Button(gridFrame,
                                    borderwidth=5,
                                    fg='red',
                                    text='New Data')
        buttonNewData.grid(row=5, column=1)
        buttonNewData.bind('<Button-1>', self.buttonNewData_cb)

        # Read data from db:
        self.dbData = Employee.read_data_from_db()

        # Display data of 1st employee '0':
        empData = self.dbData[0]
        
        name = empData[1]
        idNumber = empData[0]
        department = empData[2]
        jobTitle = empData[3]

        self.updateGui(name, idNumber, department, jobTitle)

    def buttonAddToFile_cb(self, event):
        name = self.entryName.get()
        idNumber = self.entryIdNumber.get()
        department = self.entryDepartment.get()
        jobTitle = self.entryJobTitle.get()

        emp = Employee(name, idNumber, department, jobTitle)
        emp.insert_file()

        # Clear entry values:
        self.entryName.delete(0, 'end')
        self.entryIdNumber.delete(0, 'end')
        self.entryDepartment.delete(0, 'end')
        self.entryJobTitle.delete(0, 'end')

    def buttonNewData_cb(self, event):
        self.empIndex += 1
        if self.empIndex >= len(self.dbData):
            self.empIndex = 0

        empData = self.dbData[self.empIndex]
        
        name = empData[1]
        idNumber = empData[0]
        department = empData[2]
        jobTitle = empData[3]

        self.updateGui(name, idNumber, department, jobTitle)

    def updateGui(self, name,idNumber, department, jobTitle):
        self.entryName.delete(0, 'end')
        self.entryIdNumber.delete(0, 'end')
        self.entryDepartment.delete(0, 'end')
        self.entryJobTitle.delete(0, 'end')

        self.entryName.insert(0, name)
        self.entryIdNumber.insert(0, idNumber)
        self.entryDepartment.insert(0, department)
        self.entryJobTitle.insert(0, jobTitle)

def main():
    root = tk.Tk()
    root.geometry('400x200')
    root.title('Employee')
    
    app = MainApplication(root)
    app.pack(side="top", fill="both", expand=True)

    # Remove old file if it exists:
    try:
        os.remove('Project3_Employees.txt')
    except OSError:
        pass
    
    root.mainloop()

if __name__ == '__main__':
    main()
