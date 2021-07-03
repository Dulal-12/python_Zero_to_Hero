class Calculator:
    
    def __init__(self , num):
        self.num = num
        
    def square(self):
        print(f"The value of square is {self.num**2}")
    
    def squareRoot(self):
         print(f"The value of square is {self.num**.5}")

    def cube(self):
         print(f"The value of square is {self.num**3}")

a = Calculator(9)
a.square()
a.cube()
a.squareRoot()
