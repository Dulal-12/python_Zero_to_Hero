class Employee : 
    name="Harry"
    salary = 4000
    @classmethod
    def changeSalary(cls,sal):
        cls.salary = sal
        
e = Employee()
e.changeSalary(455)
print(e.salary)
print(Employee.salary)