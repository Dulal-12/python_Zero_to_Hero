class Employee :
    company = "Google"
    salary = 5600
    bonous = 5000
    
    @property
    def totalSalary(self):
        return self.salary + self.bonous

e = Employee()
print(e.totalSalary)