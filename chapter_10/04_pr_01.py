class Programmer :
    company = "Microsoft"
    
    def __init__(self,name,product):
        
        self.name = name
        self.product = product
    
    def getInfo(self):
        
        print(f"The name of the programmer is {self.name} and comapany is {self.company} product is {self.product}")

masafir = Programmer("Mosafir" , 'Google')
akash = Programmer('Akash' , 'Skype')

masafir.getInfo()
akash.getInfo()
        