# ========
# CodeLab6
# ========

import os
import sqlite3 as lite
import sys
from contextlib import closing

class Employee:
    def __init__(self, name, idNumber, department, jobTitle):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.jobTitle = jobTitle

    def get_info(self):
        return '{},{},{},{}'.format(
            self.name,
            self.idNumber,
            self.department,
            self.jobTitle)
    
    def insert_db(self):
        con = lite.connect('CIMP8A.db')
        cur = con.cursor()
        
        cur.execute("CREATE TABLE IF NOT EXISTS Employee(Id INTEGER PRIMARY KEY, EmployeeName TEXT, EmployeeDept TEXT, JobTitle TEXT)")

        sql = '''INSERT INTO Employee (Id, EmployeeName, EmployeeDept, JobTitle)
                         VALUES (?, ?, ?, ?)'''
        cur.execute(sql, (
                    self.idNumber,
                    self.name,
                    self.department,
                    self.jobTitle))
        con.commit()

        cur.close()
        con.close()

def main():
    # Remove db if it exists
    try:
        os.remove('CIMP8A.db')
    except OSError:
        pass

    # Enter employees and save them to the db:
    while True:
        name = input('Enter Name (Press return to finish): ')
        if not name:
            break
        idNumber = int(input('Enter ID Number: '))
        department = input('Enter Department: ')
        jobTitle = input('Enter Job Title: ')

        employee = Employee(name, idNumber, department, jobTitle)

        print(employee.get_info())

        employee.insert_db()

    # Read db to verify:
    con = lite.connect('CIMP8A.db')
    cur = con.cursor()
    
    cur.execute("SELECT * FROM Employee")
    dbData = cur.fetchall()
    print(dbData)
    
    cur.close()
    con.close()

main()

    
