# Single Inheritance
class Employee :
    company = "Google"
    def show_company(self):
        print(f"I am the employee of {self.company}")
        

class Programmer(Employee):
    company = "Youtube" # It can override
    @staticmethod
    def section():
        print("You can learn everything")

obj = Programmer()
obj.show_company()