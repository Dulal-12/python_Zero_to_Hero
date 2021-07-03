#Grand-Father ----> Father ------> Children
class Mohoroddi:
    country = "Bangladesh"
    def takeBreath(self):
        print("I am brething...")
        
class Kalam(Mohoroddi):
    company = "Honda"
    
    def getSalary(self):
        print(f"Your salary is {self.salary}")
    
    def takeBreath(self):
        print("I am lucky because i am breathing.....")
   
class Dulal(Kalam):
    company = "Fiverr"
    
    def getSalary(self):
        print("No salary for Dulal")
    
    def takeBreath(self):
        super().takeBreath()
        print("I am lucky because i am breathing.....++")
        
m = Mohoroddi()
k = Kalam()
# print(k.company)
# print(k.country)
d = Dulal()
d.takeBreath()