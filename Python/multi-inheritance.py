class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"


class Developer(Employee):
    def __init__(self, name, emp_id, programming_language):
        super().__init__(name, emp_id)
        self.programming_language = programming_language


class Tester(Employee):
    def __init__(self, name, emp_id, testing_type):
        super().__init__(name, emp_id)
        self.testing_type = testing_type


class Manager(Employee):
    def __init__(self, name, emp_id):
        super().__init__(name, emp_id)
        self.managed_employees = []

    def add_employee(self, employee):
        self.managed_employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.managed_employees:
            self.managed_employees.remove(employee)
        else:
            print(f"{employee.name} not found in managed employees.")

    def display_managed_employees(self):
        print(f"Employees managed by {self.name}:")
        for emp in self.managed_employees:
            print(emp.display_info())


# Example usage:

# Creating employees
dev1 = Developer("John Doe", 101, "Python")
tester1 = Tester("Alice Smith", 102, "Manual Testing")

# Creating manager
manager = Manager("Manager Name", 100)

# Manager managing employees
manager.add_employee(dev1)
manager.add_employee(tester1)

# Displaying managed employees by manager
manager.display_managed_employees()

# Removing an employee
manager.remove_employee(dev1)

# Displaying managed employees after removal
manager.display_managed_employees()
