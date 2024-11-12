import pandas as pd

# Employee Class
class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
        self.hours_worked = 0
        self.tax_deductions = 0
        self.bonus = 0

    def calculate_net_pay(self):
        gross_pay = self.base_salary + self.bonus
        net_pay = gross_pay - self.tax_deductions
        return net_pay

    def set_hours_worked(self, hours):
        self.hours_worked = hours

    def set_tax_deductions(self, deductions):
        self.tax_deductions = deductions

    def set_bonus(self, bonus):
        self.bonus = bonus
class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_payroll(self):
        payroll_data = []
        for employee in self.employees:
            net_pay = employee.calculate_net_pay()
            payroll_data.append({
                'Employee ID': employee.emp_id,
                'Name': employee.name,
                'Net Pay': net_pay
            })
        return pd.DataFrame(payroll_data)

# Creating Employees
emp1 = Employee(1, 'Alice', 3000)
emp1.set_hours_worked(160)
emp1.set_tax_deductions(300)
emp1.set_bonus(200)

emp2 = Employee(2, 'Bob', 3500)
emp2.set_hours_worked(160)
emp2.set_tax_deductions(350)
emp2.set_bonus(250)

# Payroll System and Report
payroll = PayrollSystem()
payroll.add_employee(emp1)
payroll.add_employee(emp2)

# Generate Payroll Report
payroll_report = payroll.calculate_payroll()
print(payroll_report)
