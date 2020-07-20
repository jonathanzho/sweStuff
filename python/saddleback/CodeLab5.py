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

    print('\t' + 'No.' +
          '\t' + 'Name' +
          '\t' + 'ID Number' +
          '\t' + 'Department' +
          '\t' + 'Job Title')
    
    for e in employees:
        count += 1
        
        name = e.name
        idNumber = e.idNumber
        department = e.department
        jobTitle = e.jobTitle

        print('\t' + str(count) +
              '\t' + name +
              '\t' + str(idNumber) +
              '\t\t' + department +
              '\t\t' + jobTitle)

main()
        
        


        
                         
