class Employee:
   company = "Calendly"
   location = "Atlanta"
   emp_count = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.emp_count += 1



new_employee = Employee()
print(new_employee.location)