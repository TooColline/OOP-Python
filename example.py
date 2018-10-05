
class Employee:

    num_of_emps = 0 #class variable(shared among all instances within that class) and can be easily updated
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first #instance variable
        self.last = last
        self.pay = pay

#print(Employee.num_of_emps) will return 0 because we haven't created an employee yet

# emp_1 = Employee('Collins', 'Too', 50000)
# emp_2 = Employee('Test', 'User', 60000)

#print(Employee.num_of_emps) if we print it here it will return 2 because we have created 2 employees so far

# print(emp_1) to check the object infor
# print(emp_2)

# print('{} {}'.format(emp_1.first, emp_1.last)) tiresome to print fullname like this, try below

    def fullname(self):
        return '{} {}'.format(self.first, self.last) #so that it works with all instances

# print(emp_1.fullname()) 
# print(Employee.fullname(emp_1)) if we print out emp from class we have to manually pass an instance to it

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #using class variable, access it thru 'self' instance to give us the ability to change that amount for a single instance if we wanted to or Employee class by saying Employee.raise_amount

#instead of
#   def apply_raise(self):
#       self.pay = int(self.pay * 1.04)


    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

# print(emp_1.email)
# print(emp_2.email)

    def __repr__(self): #unambiguous rep of object used for debugging and login by other developers
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

# print(repr(emp_1)) it should return the string you specified in the __repr__ method

    def __str__(self): #readable rep of object meant to be used by end user
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

# print(emp_1 + emp_2)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
#The above @classmethod enables us pass the raise amount as: Employee.set_raise_amt(1.05) or from the instance as: emp_1.set_raise_amt(1.05)

    @classmethod #using this method as an alternative constructor. Check the datetime module online to understand more
    def from_string(cls, emp_str): #usually takes the 'from' by convention but let's just call this from_string
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #this line return that new employee that we've created

    @staticmethod #does not depend on any instance or class but just has a logical relationship to the class
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

#confirm with below code if @staticmethod is working
# import datetime
# my_date = datetime.date(2018, 10, 10)

# print(Employee.is_workday(my_date))

class Developer(Employee):

    raise_amount = 1.10 #by changing the raise amt in subclass it wouldn't have an effect on employee class

    def __init__(self, first, last, pay, prog_lang): #initiating subclass with more information our superclass can handle
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

# dev_1 = Developer('Collins', 'Too', 50000, 'Python')
# dev_2 = Developer('Test', 'User', 60000, 'Java')

# print(dev_1.email)
# print(dev_1.prog_lang)

class Manager(Employee):

    def __init__(self, first, last, pay, employees =None): #not passing mutable data types as default
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
#mgr_1.add_emp(dev_2)
#mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

#check below built in functions as well
# print(isinstance(mgr_1, Manager)) should return True
# print(isinstance(mgr_1, Developer)) should return False
# print(issubclass(Developer, Employee)) should return True
# print(issubclass(Manager, Employee)) should return True
# print(issubclass(Manager, Developer)) should return True