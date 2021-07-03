class Employee:
    company = "Google"
    
    def getSalary(self):
        print(f"Your salary is {self.salary}k and company is {self.company}")
        
    @staticmethod
    def greet():
        print("Good m9 , sir")
        
dulal = Employee()
dulal.salary = 100
# dulal.getSalary() # Employee.getSalary(harry)
dulal.greet()