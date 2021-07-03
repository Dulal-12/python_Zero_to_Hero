class Dulali:
    taka = 6
class Kalam:
    company = "Google"
    
class Programmer(Dulali , Kalam):
    def upgradeTaka(self):
        self.taka = self.taka + 1
        print(f"My comapany name is {self.company} and taka is {self.taka}")

Dulal = Programmer()
Dulal.upgradeTaka()