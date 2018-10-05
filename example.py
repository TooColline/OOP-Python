
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees =None):
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

# emp_1 = Employee('Collins', 'Too', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# print(emp_1 + emp_2)

# dev_1 = Developer('Collins', 'Too', 50000, 'Python')
# dev_2 = Developer('Test', 'User', 60000, 'Java')

# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Developer))
# print(issubclass(Developer, Employee))


# print(dev_1.email)
# print(dev_1.prog_lang)


# import datetime
# my_date = datetime.date(2018, 10, 10)

# print(Employee.is_workday(my_date))