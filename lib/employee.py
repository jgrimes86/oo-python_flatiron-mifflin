class Employee:
    
    all = []

    def __init__(self, name, salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager
        self.all.append(self)
    
    @classmethod
    def paid_over(cls, number):
        return [employee for employee in cls.all if employee.salary > number]

    @classmethod
    def find_by_department(cls, department):
        # dept_manager = [manager for manager in Manager.all if manager.department == department]
        employees = [employee for employee in cls.all if employee.manager.department == department]
        return employees[0]
    
    def tax_bracket(self):
        lower_filter = [employee for employee in Employee.all if employee.salary >= (self.salary-1000)]
        upper_filter = [employee for employee in lower_filter if employee.salary <= (self.salary+1000)]
        return [employee for employee in upper_filter if employee != self]
