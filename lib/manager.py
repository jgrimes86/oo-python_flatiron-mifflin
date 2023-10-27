from lib.employee import Employee

class Manager:
    
    all = []

    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
        self.all.append(self)
    
    def employees(self):
        return [employee for employee in Employee.all if employee.manager == self]

    def hire_employee(self, employee_name, salary):
        Employee(employee_name, salary, self)

    @classmethod
    def all_departments(cls):
        return [manager.department for manager in cls.all]

    @classmethod
    def average_age(cls):
        ages = [manager.age for manager in cls.all]
        total_age = 0
        for age in ages:
            total_age += age
        return float(total_age / (len(ages)))
    
