# ============
# Test classes
# ============

# A class which does nothing:

# 1============================================================================
class DoNothing:
    pass

# 2============================================================================
# A parent/base class:

class Employee:
    # class variable:
    count = 0
    
    # class constructor:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        # Change class variable:
        Employee.count += 1
        
    # instance method:
    def get_info(self):
        return '{},{},{}'.format(self.name, self.email, self.role)

# 3============================================================================
# A child/derived class - single inheritance:

class Receptionist(Employee):
    def __init__(self, name, email, role, foreignLanguage):
        super().__init__(name, email, role)
        self.foreignLanguage = foreignLanguage

    def get_info(self):
        return '{},{},{}, {}'.format(self.name, self.email, self.role,
                                     self.foreignLanguage)

# 4============================================================================
# A child/derived class - multiple inheritance:

class Equipment:
    def __init__(self, equipType, equipOwner):
        self.equipType = equipType
        self.equipOwner = equipOwner
    def get_info(self):
        return 'equipment type: {}, owned by: {}'.format(self.equipType,
                                                         self.equipOwner)

class Developer(Employee, Equipment):
    def __init__(self, name, email, role,
                 equipType, equipOwner,
                 progLanguage):
        super().__init__(name, email, role)
        self.equipType = equipType
        self.equipOwner = equipOwner
        self.progLanguage = progLanguage

    def get_info(self):
        return '{},{},{},{},{},{}'.format(self.name, self.email, self.role,
                                          self.equipType, self.equipOwner,
                                          self.progLanguage)

# 5============================================================================
# Data encapsulation

class Person:
    def __init__(self, name, age, weight):
        # public data:
        self.name = name
        # private data (using accessers)
        self._age = age
        # private data (using property)
        self._weight = weight

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def delete_age(self):
        del self._age
        
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @weight.deleter
    def weight(self):
        del self._weight

# =============================================================================
# 1============================================================================
# Test class DoNothing

doNothing1 = DoNothing()
print(doNothing1)

# 2============================================================================
# Test base class

employee1 =  Employee('John Smith', 'jsmith@abc.com', 'CEO')
print(employee1.get_info())
print(Employee.count)

# 3============================================================================
# Test single inheritance

receptionist1 = Receptionist('Sarah Jones', 'sjones@abc.com', 'Receptionist',
                              'Spanish')
print(receptionist1.get_info())
print(Employee.count)

# 4============================================================================
# Test multiple inheritance

equipment1 = Equipment('MacBoook Pro', 'Company')
print(equipment1.get_info())

developer1 = Developer('Mike Wang', 'mwang@abc.com', 'Senior Developer',
                       equipment1.equipType, equipment1.equipOwner,
                       'Python')
print(developer1.get_info())
print(Employee.count)

# 5=============================================================================
# Test data encapsulation

# Initial values:
person1 = Person('Mike', 17, 100.0)
print(person1.name, person1.get_age(), person1.weight)

# Change values:
person1.name = 'Michael'
person1.set_age(18)
person1.age = 19 # This will be ignored !!!
person1.weight = 110.0
print(person1.name, person1.get_age(), person1.weight)

# Delete variables:
del person1.name
person1.delete_age()
del person1.weight
# AttributionError:
#print(person1.name, person1.get_age(), person1.weight)



