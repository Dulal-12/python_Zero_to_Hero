class Employee:
    company = "Google"
    
    def __init__(self,name,salary , subunit) :
        self.name = name
        self.salary = salary
        self.subunit = subunit
        
    def getSalary(self):
        print(f"Your salary is {self.salary}k and company is {self.company} and section is {self.subunit}")

dulal = Employee("Musafir" , '100k' , 'web developer')
dulal.getSalary()