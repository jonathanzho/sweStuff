#===========
# Code Lab 5
#===========

class Employee:
    def __init__(self, name, idNumber, department, jobTitle):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.jobTitle = jobTitle

def main():
    employees = []
    
    while True:
        name = input('Enter employee Name (return to stop): ')
        if name == '':
            break
        idNumber = int(input('Enter employee ID Number: ' ))
        department = input('Enter employee Department: ')
        jobTitle = input('Enter employee Job Title: ')
        employees.append(Employee(name,
                                  idNumber,
                                  department,
                                  jobTitle)
                         )

    displayEmployees(employees)

def displayEmployees(employees):
    count = 0;

    print('No.'.ljust(10) +
          'Name'.ljust(20) +
          'ID Number'.ljust(10) +
          'Department'.ljust(20) +
          'Job Title'.ljust(20))
    print('-'*80)
    
    for e in employees:
        count += 1
        
        name = e.name
        idNumber = e.idNumber
        department = e.department
        jobTitle = e.jobTitle

        print(str(count).ljust(10) +
              name.ljust(20) +
              str(idNumber).ljust(10) +
              department.ljust(20) +
              jobTitle.ljust(20))

main()
        
        


        
                         
